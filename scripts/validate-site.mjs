import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { extname, join, relative, resolve } from 'node:path';

const root = resolve(import.meta.dirname, '..');
const dist = join(root, 'dist');
const failures = [];

const expect = (condition, message) => {
  if (!condition) failures.push(message);
};

const walk = (directory) =>
  readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const path = join(directory, entry.name);
    return entry.isDirectory() ? walk(path) : [path];
  });

const bannedTerms = [
  String.fromCharCode(84, 105, 118, 111, 108, 105),
  String.fromCharCode(73, 80, 84, 86),
];

expect(existsSync(join(dist, 'index.html')), 'Missing generated home page.');
expect(
  existsSync(join(dist, 'documents', 'Ahmed-Mohamed-Noaman-CV.pdf')),
  'Missing public CV.',
);
expect(existsSync(join(dist, 'og.png')), 'Missing social-sharing image.');
expect(existsSync(join(dist, 'sitemap.xml')), 'Missing sitemap.');
expect(existsSync(join(dist, 'robots.txt')), 'Missing robots file.');

const files = walk(dist);
const htmlFiles = files.filter((file) => extname(file) === '.html');
expect(
  htmlFiles.length === 9,
  `Expected 9 generated HTML pages; found ${htmlFiles.length}.`,
);

const resolvePublicReference = (reference) => {
  const clean = reference.split(/[?#]/, 1)[0];
  if (
    !clean ||
    clean.startsWith('#') ||
    /^(https?:|mailto:|tel:|data:)/.test(clean)
  )
    return null;
  const pathname = clean.startsWith('/') ? clean.slice(1) : clean;
  const direct = join(dist, pathname);
  if (existsSync(direct) && statSync(direct).isFile()) return direct;
  const indexFile = join(direct, 'index.html');
  if (existsSync(indexFile)) return indexFile;
  if (!extname(direct)) {
    const htmlFile = `${direct}.html`;
    if (existsSync(htmlFile)) return htmlFile;
  }
  return direct;
};

for (const file of htmlFiles) {
  const source = readFileSync(file, 'utf8');
  expect(
    source.includes('<meta name="description"'),
    `${relative(dist, file)} lacks a description.`,
  );
  expect(
    source.includes('<link rel="canonical"'),
    `${relative(dist, file)} lacks a canonical URL.`,
  );
  expect(
    source.includes('Skip to main content'),
    `${relative(dist, file)} lacks the skip link.`,
  );
  expect(
    !source.includes('autoplay'),
    `${relative(dist, file)} contains autoplay media.`,
  );
  expect(
    !/\+20[\s()-]*\d{3}[\s()-]*\d{3}[\s()-]*\d{4}/.test(source),
    `${relative(dist, file)} exposes a phone number.`,
  );
  for (const term of bannedTerms) {
    expect(
      !source.toLowerCase().includes(term.toLowerCase()),
      `${relative(dist, file)} contains excluded content.`,
    );
  }
  for (const match of source.matchAll(/(?:href|src|poster)="([^"]+)"/g)) {
    const target = resolvePublicReference(match[1]);
    if (target)
      expect(
        existsSync(target),
        `${relative(dist, file)} references missing ${match[1]}.`,
      );
  }
  for (const match of source.matchAll(
    /\/(?:assets|documents)\/[A-Za-z0-9_./-]+\.(?:avif|webp|png|jpg|jpeg|svg|mp4|webm|pdf)/gi,
  )) {
    const target = resolvePublicReference(match[0]);
    if (target)
      expect(
        existsSync(target),
        `${relative(dist, file)} references missing ${match[0]}.`,
      );
  }
}

const home = readFileSync(join(dist, 'index.html'), 'utf8');
const initialBlock = home.split('id="additional-projects"')[0];
expect(
  (initialBlock.match(/<article class="project-card(?:\s|")/g) ?? []).length ===
    3,
  'The initial projects section must contain exactly three project cards.',
);
expect(
  home.includes('id="additional-projects"') && home.includes(' hidden'),
  'Additional projects are not hidden initially.',
);
expect(
  home.includes('aria-expanded="false"') &&
    home.includes('aria-controls="additional-projects"'),
  'Projects toggle accessibility state is missing.',
);
expect(
  home.includes(
    'Independent educational project; not affiliated with Instagram or Meta.',
  ),
  'Independent-project disclaimer is missing.',
);
expect(home.includes('UI-Only Project'), 'UI-only project label is missing.');

const thumbnails = [
  'strong-8k',
  'khayyer',
  'psa-academy',
  'padel-system',
  'ecommerce',
  'instagram-clone',
  'food-delivery-ui',
  'todo',
];
for (const slug of thumbnails) {
  expect(
    existsSync(join(dist, 'assets', 'projects', slug, 'thumbnail.webp')),
    `Missing ${slug} WebP thumbnail.`,
  );
  expect(
    existsSync(join(dist, 'assets', 'projects', slug, 'thumbnail.avif')),
    `Missing ${slug} AVIF thumbnail.`,
  );
}

expect(
  !files.some((file) => extname(file).toLowerCase() === '.apk'),
  'APK files must not be committed to the static site.',
);

if (failures.length) {
  console.error(`Validation failed (${failures.length}):`);
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exit(1);
}

console.log(
  `Validated ${htmlFiles.length} pages and ${files.length} generated files.`,
);
