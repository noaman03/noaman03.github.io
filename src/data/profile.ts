export const profile = {
  name: 'Ahmed Mohamed Noaman',
  shortName: 'Ahmed Noaman',
  title: 'Flutter Developer & Mobile Application Engineer',
  location: 'Cairo, Egypt',
  email: 'noamana455@gmail.com',
  github: 'https://github.com/noaman03',
  linkedin: 'https://www.linkedin.com/in/ahmed-noaman-07ab162b4',
  site: 'https://noaman03.github.io',
  cv: '/documents/Ahmed-Mohamed-Noaman-CV.pdf',
} as const;

/**
 * Skills that appear in shipped or published work. The DevOps diploma material
 * that has not been used in a shipped project lives in `studied` below, because
 * this site draws that line everywhere else and should draw it here too.
 */
export const expertise = [
  {
    title: 'Mobile development',
    skills: [
      'Flutter',
      'Dart',
      'Kotlin platform views',
      'Swift',
      'Android TV and D-pad navigation',
      'Media3/ExoPlayer and libmpv',
      'Responsive and RTL UI',
    ],
  },
  {
    title: 'Architecture',
    skills: [
      'Feature-first Clean Architecture',
      'Layered UI, domain, and data design',
      'SOLID principles',
      'Functional programming',
      'Dartz',
    ],
  },
  {
    title: 'State management',
    skills: ['Riverpod', 'BLoC', 'Cubit', 'Provider', 'GetX'],
  },
  {
    title: 'Backend and data',
    skills: [
      'Firebase',
      'Supabase',
      'Supabase Realtime',
      'Cloud Firestore',
      'SQLite',
      'MySQL',
      'Node.js',
      'Express',
    ],
  },
  {
    title: 'Integrations',
    skills: [
      'REST APIs',
      'WebSockets',
      'Push notifications',
      'Geolocation',
      'Biometric authentication',
      'QR scanning',
      'PDF generation',
      'File and image uploads',
    ],
  },
  {
    title: 'Specialized technology',
    skills: [
      'YOLOv8',
      'Computer vision',
      'Web3dart',
      'Blockchain integration',
      'Real-time communications',
    ],
  },
  {
    title: 'Delivery',
    skills: [
      'Linux (Ubuntu, systemd, nginx)',
      'Codemagic CI',
      'GitHub Actions',
      'Google Play and Microsoft Store releases',
      'White-label build tooling',
    ],
  },
  {
    title: 'Engineering tools',
    skills: ['Git', 'GitHub', 'Postman', 'Testing', 'Quality assurance'],
  },
  {
    title: 'Security and networking',
    skills: [
      'Cisco CyberOps',
      'CCNA',
      'Identity and Access Management',
      'Secure-by-design development',
    ],
  },
] as const;

/**
 * Covered by the Andalusia DevOps Engineering diploma but not used in any
 * project on this site. Listed separately rather than mixed into `expertise`,
 * for the same reason Khayyer's YOLOv8 and blockchain work is marked as
 * research scope: the site only claims what it can show.
 */
export const studied = {
  note: 'From the DevOps Engineering diploma, Andalusia, 2026. None of it appears in the work below — Strong 8K runs on plain Linux, systemd and nginx.',
  skills: [
    'Docker',
    'Kubernetes',
    'Terraform',
    'Ansible',
    'Jenkins',
    'Argo CD',
    'Prometheus',
    'Grafana',
    'AWS',
    'Azure',
  ],
} as const;

export const certifications = [
  'Flutter Diploma — AMIT Learning — Grade 95%',
  'DevOps Engineering Diploma — Andalusia — 2026',
  'Developing iOS Applications with Swift — ITI',
  'Developing Back-End Apps with Node.js and Express — IBM',
  'Quality Assurance — Techniques and Methodologies',
  'Cisco Certified CyberOps Associate — NTI/Cisco',
  'CCNAv7 Enterprise Networking, Security, and Automation — Cisco',
  'CCNAv7 Switching, Routing, and Wireless Essentials — Cisco',
  'Identity and Access Management — Professional Diploma',
] as const;

export const secondaryCertifications = [
  'Database Technologies and Services — Professional Diploma',
  'Artificial Intelligence: Basic Level — WE Certificate',
  'Cloud Computing — Professional Certificate',
  'Project Management in Practice — Professional Diploma',
] as const;
