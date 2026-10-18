export type ProjectImage = {
  src: string;
  srcSet?: string;
  width: number;
  height: number;
  alt: string;
};

export type ProjectLink = {
  label: string;
  url: string;
};

export type Project = {
  slug: string;
  name: string;
  title: string;
  category: string;
  summary: string;
  overview: string[];
  featured: boolean;
  status: string;
  labels: string[];
  stack: string[];
  highlights: string[];
  architecture: string;
  /** Public source repository. Omitted for client-owned, private code. */
  repository?: string;
  /** Store listings, product sites, and other external links. */
  links?: ProjectLink[];
  /** Platforms the application ships on, for structured data. */
  platforms?: string;
  liveUrl?: string;
  apkUrl?: string;
  video?: string;
  videoType?: string;
  thumbnail: ProjectImage;
  gallery: ProjectImage[];
  note?: string;
  disclaimer?: string;
  funding?: {
    statement: string;
    url: string;
  };
};

const projectAsset = (slug: string, file: string) =>
  `/assets/projects/${slug}/${file}`;

export const projects: Project[] = [
  {
    slug: 'strong-8k',
    name: 'Strong 8K',
    title:
      'Strong 8K — Live TV and On-Demand Streaming Client for Android, Android TV and Windows',
    category: 'Freelance · Streaming & Media Player',
    summary:
      'A white-label streaming player delivered end to end as a freelance engagement: live TV, movies, series, radio, EPG, time-shift and catch-up on Android phones, tablets, TV boxes and Windows, published on Google Play and the Microsoft Store.',
    overview: [
      'Strong 8K activates a device against a reseller panel or signs in to an Xtream Codes line, then plays live television, on-demand movies and series, radio, a programme guide, time-shift and catch-up. One Flutter UI drives two playback engines: Media3/ExoPlayer through a native Kotlin platform view on Android, and libmpv through media_kit on Windows. The interface is built for landscape, D-pad navigation and three locales including right-to-left Arabic.',
      'The engagement ran from July to October 2026 as sole developer: 195 commits, 173 Dart files, 51 screens and a test suite that grew with the code to 2,603 passing tests. Alongside the client it included a Node.js reviewer demo service deployed on Ubuntu behind nginx and TLS, a React admin portal, a white-label build driver that produces fifteen brand configurations from one codebase, and a Codemagic pipeline that verifies the produced binary is a genuine release build. The source is client-owned and private; this page links to the store listing and reviewed screenshots instead.',
    ],
    featured: true,
    status: 'Published on Google Play and the Microsoft Store',
    labels: ['Featured Project', 'Freelance', 'Published'],
    stack: [
      'Flutter',
      'Dart',
      'Kotlin',
      'Media3/ExoPlayer',
      'libmpv',
      'Node.js',
      'nginx',
    ],
    highlights: [
      'Ships one UI over two playback engines: Media3/ExoPlayer via a Kotlin platform view on Android and libmpv via media_kit on Windows.',
      'Server failover that tells a blocked host from an expired subscription, authenticating candidates concurrently and keeping the operator’s priority order.',
      'A playback watchdog fed by decoder frame counters across the platform channel, so a frozen picture with live audio is detected and recovered.',
      'A ~27 MB offline catalogue synced by delta in isolate workers with single-flight, crash-safe writes, keeping weak TV boxes responsive.',
      'A 2,600-line Node.js demo service for store reviewers with timing-safe auth, deployed by an idempotent installer and verified by a post-deploy smoke test.',
      'A white-label build driver and Codemagic CI pipeline that run 2,600+ tests and assert the output is a real release build before packaging.',
    ],
    architecture:
      'Deliberately plain layering: one Session ChangeNotifier for application state, Provider at the root, static service singletons over SharedPreferences and JSON files, Navigator 1.0, no DI container and no code generation. Brand identity, palette and feature toggles are injected at build time from a per-client config file.',
    platforms: 'Android, Android TV, Windows',
    links: [
      {
        label: 'Google Play',
        url: 'https://play.google.com/store/apps/details?id=com.strong8k.player_desktop',
      },
      {
        label: 'Microsoft Store',
        url: 'https://apps.microsoft.com/detail/9NMC00K9G60N',
      },
    ],
    thumbnail: {
      src: projectAsset('strong-8k', 'thumbnail.webp'),
      srcSet: `${projectAsset('strong-8k', 'thumbnail-640.webp')} 640w, ${projectAsset('strong-8k', 'thumbnail.webp')} 1200w`,
      width: 1200,
      height: 675,
      alt: 'Strong 8K gold logo and wordmark with the tagline "Your media. Every screen." on a dark background.',
    },
    gallery: [
      [
        'strong8k-home',
        1200,
        675,
        'Strong 8K home screen with an active subscription badge, featured title, and Live, Movies, Series and Radio tiles.',
      ],
      [
        'strong8k-live-tv',
        1200,
        675,
        'Live TV channel list with search, live indicators and a channel preview pane.',
      ],
      [
        'strong8k-movies',
        1200,
        675,
        'Movies browse with category chip, search, sort filters, genre dropdown and poster grid.',
      ],
      [
        'strong8k-movie-details',
        1200,
        675,
        'Movie detail page with genre and rating chips, Watch Now, favourite and download actions and a cast row.',
      ],
      [
        'strong8k-player',
        1200,
        675,
        'Fullscreen video player with transport controls, scrubber and quality badge.',
      ],
      [
        'strong8k-series',
        1200,
        675,
        'Series browse with featured, new, top-rated and alphabetical filters.',
      ],
      [
        'strong8k-tablet-home',
        1200,
        750,
        'Home screen in the ten-inch tablet layout.',
      ],
      [
        'strong8k-tablet-live',
        1200,
        750,
        'Live channel playback with the now-and-next programme bar in the tablet layout.',
      ],
      [
        'strong8k-tablet-series',
        1200,
        750,
        'Series detail with season picker and episode list in the tablet layout.',
      ],
    ].map(([file, width, height, alt]) => ({
      src: projectAsset('strong-8k', `${file}.webp`),
      srcSet: `${projectAsset('strong-8k', `${file}-480.webp`)} 480w, ${projectAsset('strong-8k', `${file}.webp`)} 1200w`,
      width: width as number,
      height: height as number,
      alt: alt as string,
    })),
    note: 'Screenshots were captured against the purpose-built reviewer demo line, so the catalogue is Blender open movies under CC-BY and no customer data appears. Published on Google Play and the Microsoft Store; an App Store release is in preparation. The client code is private and client-owned.',
  },
  {
    slug: 'khayyer',
    name: 'Khayyer',
    title: 'Khayyer — Food Donation and Transparent Logistics Platform',
    category: 'Graduation Project · Food Donation',
    summary:
      'A bilingual Flutter application that connects food donors with charitable organizations through donation capture, campaigns, location-aware coordination, and status updates.',
    overview: [
      'Khayyer brings donor, organization, and registered-recipient workflows into one Flutter application. The public repository verifies account flows, Firestore-backed records, media uploads, location capture, campaigns, bilingual content, and notification setup.',
      'The graduation-project CV describes a broader research scope involving YOLOv8 freshness checks and blockchain-backed traceability. The current public code snapshot does not contain a YOLOv8 model or a production smart-contract write, so those concepts are documented as project scope rather than shipped repository features.',
    ],
    featured: true,
    status: 'Graduation project · Portfolio build',
    labels: ['Featured Project', 'Graduation Project', 'Funded by ITIDA'],
    stack: [
      'Flutter',
      'Dart',
      'GetX',
      'Firebase',
      'Cloud Firestore',
      'Geolocator',
    ],
    highlights: [
      'Structured donor, organization, and recipient flows around controllers, repositories, models, and views.',
      'Connected Firebase authentication, Firestore records, Storage uploads, and Google sign-in.',
      'Captured donation media and GPS location with campaign and status workflows.',
      'Added English and Arabic localization with saved language and theme preferences.',
      'Prepared FCM token handling and local-notification infrastructure.',
    ],
    architecture:
      'Controller, repository, model, service, and view layers with GetX state and GetStorage preferences.',
    repository: 'https://github.com/noaman03/khayyer-food-donation',
    apkUrl:
      'https://github.com/noaman03/khayyer-food-donation/releases/download/v1.0.0-demo.1/Khayyer-v1.0.0-demo.1.apk',
    video: projectAsset('khayyer', 'khayyer-demo.mp4'),
    videoType: 'video/mp4',
    thumbnail: {
      src: projectAsset('khayyer', 'thumbnail.webp'),
      srcSet: `${projectAsset('khayyer', 'thumbnail-640.webp')} 640w, ${projectAsset('khayyer', 'thumbnail.webp')} 1200w`,
      width: 1200,
      height: 675,
      alt: 'Khayyer logo and loading screen displayed in a mobile phone frame.',
    },
    gallery: [
      {
        src: projectAsset('khayyer', 'khayyer-onboarding.webp'),
        srcSet: `${projectAsset('khayyer', 'khayyer-onboarding-480.webp')} 480w, ${projectAsset('khayyer', 'khayyer-onboarding.webp')} 1200w`,
        width: 1200,
        height: 675,
        alt: 'Khayyer onboarding screens introducing food donation and community support.',
      },
      {
        src: projectAsset('khayyer', 'khayyer-donation-flow.webp'),
        srcSet: `${projectAsset('khayyer', 'khayyer-donation-flow-480.webp')} 480w, ${projectAsset('khayyer', 'khayyer-donation-flow.webp')} 1200w`,
        width: 1200,
        height: 675,
        alt: 'Khayyer donor flow with food details, assessment result, and donation tracking.',
      },
      {
        src: projectAsset('khayyer', 'khayyer-charity-scheduling.webp'),
        srcSet: `${projectAsset('khayyer', 'khayyer-charity-scheduling-480.webp')} 480w, ${projectAsset('khayyer', 'khayyer-charity-scheduling.webp')} 1200w`,
        width: 1200,
        height: 675,
        alt: 'Khayyer charity workflow with notifications, donation acceptance, and pickup scheduling.',
      },
    ],
    note: 'Implementation note: the repository declares Web3dart but does not perform an on-chain write; its 0x identifier is SHA-256-derived. The repository also does not include the CV-referenced YOLOv8 model.',
    funding: {
      statement:
        'Khayyer is Ahmed Noaman’s graduation project and received funding from ITIDA, Egypt’s Information Technology Industry Development Agency.',
      url: 'https://www.itida.gov.eg/English/Pages/about-itida.aspx',
    },
  },
  {
    slug: 'psa-academy',
    name: 'PSA Academy',
    title: 'PSA Academy — Sports Academy Management and Analytics',
    category: 'Sports Management & Analytics',
    summary:
      'A Flutter Web and Firebase platform for academy roles, athlete attendance, training plans, operational records, and PDF reporting.',
    overview: [
      'PSA Academy digitizes day-to-day academy operations for administrators, coaches, and players. It brings attendance, training assignments, work sessions, payments, expenses, and reporting into a role-aware Flutter Web experience.',
      'The repository is transitioning toward layered architecture: newer core, data, domain, and presentation modules coexist with legacy pages and services. The portfolio describes that state directly rather than presenting the migration as complete.',
    ],
    featured: true,
    status: 'Hosted portfolio application',
    labels: ['Featured Project'],
    stack: [
      'Flutter Web',
      'Firebase',
      'Provider',
      'Cloud Firestore',
      'QR scanning',
      'PDF',
    ],
    highlights: [
      'Routes administrators, coaches, and players into role-specific academy workflows.',
      'Supports QR generation and camera scanning for attendance workflows.',
      'Manages training templates, player assignments, work sessions, payments, and expenses.',
      'Generates PDF reports and browser downloads for operational records.',
      'Uses Provider/ChangeNotifier with SharedPreferences and declared Dartz error-handling primitives.',
    ],
    architecture:
      'An in-progress layered migration with core/data/domain/presentation modules alongside legacy pages, services, and use cases.',
    repository: 'https://github.com/noaman03/psa-fitness-academy',
    liveUrl: 'https://psa-academy-65088.web.app/',
    thumbnail: {
      src: projectAsset('psa-academy', 'thumbnail.webp'),
      srcSet: `${projectAsset('psa-academy', 'thumbnail-640.webp')} 640w, ${projectAsset('psa-academy', 'thumbnail.webp')} 1200w`,
      width: 1200,
      height: 675,
      alt: 'PSA Academy loading screen preparing the academy dashboard.',
    },
    gallery: [
      {
        src: projectAsset('psa-academy', 'psa-athlete-workout.webp'),
        width: 480,
        height: 874,
        alt: 'PSA Academy player workout details and exercise plan.',
      },
      {
        src: projectAsset('psa-academy', 'psa-qr-attendance.webp'),
        width: 480,
        height: 874,
        alt: 'PSA Academy coach and player QR attendance workflow.',
      },
      {
        src: projectAsset('psa-academy', 'psa-admin-analytics.webp'),
        width: 480,
        height: 874,
        alt: 'PSA Academy administrator analytics and quick actions.',
      },
      {
        src: projectAsset('psa-academy', 'psa-finance-overview.webp'),
        width: 480,
        height: 874,
        alt: 'PSA Academy payment and expense management overview.',
      },
    ],
    note: 'Security note: application role checks do not replace backend authorization, and repository security rules are not included in the public snapshot.',
  },
  {
    slug: 'padel-system',
    name: 'Padel System',
    title: 'Padel System — Court Booking and Club Management Application',
    category: 'Booking & Club Management',
    summary:
      'A Flutter application for court discovery and booking, open matches, tournaments, player chat, and venue-owner and administrator operations, with complete light and dark themes.',
    overview: [
      'Padel System covers the workflows needed by players, venue owners, and administrators: court discovery, reservations, tournaments, open-match creation and joining, player chat, and operational dashboards with court and tournament editors.',
      'The current main branch is an offline-capable portfolio demo. Firestore-backed court discovery and booking-record paths exist, while login uses one-tap demo roles and chat, matches, tournaments, and owner management run on session-persistent in-memory stores rather than a backend.',
    ],
    featured: false,
    status: 'Portfolio prototype',
    labels: ['Portfolio Prototype'],
    stack: [
      'Flutter',
      'Dart',
      'Firebase',
      'Cloud Firestore',
      'GetX',
      'Riverpod',
    ],
    highlights: [
      'Organizes player, owner, and administrator experiences into feature-oriented Flutter modules.',
      'Implements Firestore court discovery, search, and booking-record paths.',
      'Provides open-match creation, join requests, and session-persistent player chat backed by shared in-memory stores.',
      'Includes owner dashboards with court and tournament editor screens.',
      'Ships complete light and dark themes with one-tap demo accounts for the player, owner, and administrator roles.',
    ],
    architecture:
      'Feature-oriented auth, player, and owner modules with a mixed GetX/Riverpod state-management approach.',
    repository: 'https://github.com/noaman03/padel-management-system',
    apkUrl:
      'https://github.com/noaman03/padel-management-system/releases/download/v1.0.0-demo.1/Padelit-v1.0.0-demo.1.apk',
    video: projectAsset('padel-system', 'padel-demo.mp4'),
    videoType: 'video/mp4',
    thumbnail: {
      src: projectAsset('padel-system', 'thumbnail.webp'),
      srcSet: `${projectAsset('padel-system', 'thumbnail-640.webp')} 640w, ${projectAsset('padel-system', 'thumbnail.webp')} 1200w`,
      width: 1200,
      height: 675,
      alt: 'Padelit project cover for court booking, open matches, tournaments, and club management.',
    },
    gallery: [
      [
        'padel-home',
        'Player home with court booking, next match, reservations, and popular courts.',
      ],
      [
        'padel-home-dark',
        'Player home in the dark theme with booking shortcuts and reservations.',
      ],
      [
        'padel-courts',
        'Court discovery list with availability and venue information.',
      ],
      [
        'padel-tournaments',
        'Tournament browsing screen with official and community events.',
      ],
      [
        'padel-tournament-details',
        'Tournament details with schedule and participation information.',
      ],
      ['padel-matches', 'Open matches list with joinable community games.'],
      [
        'padel-match-details',
        'Open match details with roster and joining information.',
      ],
      ['padel-chat-dark', 'Player chat conversation in the dark theme.'],
      [
        'padel-owner-dashboard',
        'Venue-owner dashboard summarizing operational activity.',
      ],
      ['padel-owner-courts', 'Venue-owner court management screen.'],
      [
        'padel-admin-dashboard',
        'Administration dashboard with operational summaries.',
      ],
    ].map(([file, alt]) => ({
      src: projectAsset('padel-system', `${file}.webp`),
      srcSet: `${projectAsset('padel-system', `${file}-480.webp`)} 480w, ${projectAsset('padel-system', `${file}.webp`)} 828w`,
      width: 828,
      height: 1792,
      alt,
    })),
    note: 'Demo boundary: authentication uses one-tap demo roles and payment is simulated; chat, matches, tournaments, and owner management persist in session memory rather than a backend.',
  },
  {
    slug: 'ecommerce',
    name: 'E-commerce Application',
    title: 'A-store — Offline E-commerce Application',
    category: 'Shopping Application',
    summary:
      'An offline Flutter storefront and administration demo with product variations, cart, checkout, orders, and seeded local data.',
    overview: [
      'A-store demonstrates both sides of a commerce experience: customers can browse a seeded catalogue, manage product choices, cart and wishlist state, and move through checkout, while an admin interface manages catalogue and order data.',
      'The project is intentionally offline. It uses GetStorage as a local JSON document store and does not connect to a backend, payment provider, social sign-in service, or email delivery system.',
    ],
    featured: false,
    status: 'Offline portfolio application',
    labels: [],
    stack: ['Flutter', 'Dart', 'GetX', 'GetStorage', 'Local data'],
    highlights: [
      'Implements catalogue, product-variation, cart, wishlist, checkout, order, profile, and address flows.',
      'Includes an administration interface for products, customers, categories, brands, banners, and orders.',
      'Persists seeded demonstration data locally through GetStorage.',
      'Separates bindings, models, repositories, services, features, routes, and shared widgets.',
      'Commits 57 declared unit and widget tests across model, data, flow, and screen suites.',
    ],
    architecture:
      'Feature-oriented GetX application with data models, repositories, services, bindings, routes, and shared widgets.',
    repository: 'https://github.com/noaman03/AA-e-commerce',
    apkUrl:
      'https://github.com/noaman03/AA-e-commerce/releases/download/v1.0.0-demo.1/A-store-v1.0.0-demo.1.apk',
    video: projectAsset('ecommerce', 'ecommerce-demo.mp4'),
    videoType: 'video/mp4',
    thumbnail: {
      src: projectAsset('ecommerce', 'thumbnail.webp'),
      srcSet: `${projectAsset('ecommerce', 'thumbnail-640.webp')} 640w, ${projectAsset('ecommerce', 'thumbnail.webp')} 1200w`,
      width: 1200,
      height: 675,
      alt: 'A-store home screen presented in a branded shopping application cover.',
    },
    gallery: [
      [
        'ecommerce-home',
        'A-store storefront home with product collections and navigation.',
      ],
      [
        'ecommerce-product-detail',
        'A-store product details with variations and purchase controls.',
      ],
      [
        'ecommerce-products-grid',
        'A-store dark product grid with categories and filtering controls.',
      ],
      [
        'ecommerce-admin-dashboard',
        'A-store admin dashboard with local catalogue summaries.',
      ],
      [
        'ecommerce-admin-products',
        'A-store administration view for product management.',
      ],
    ].map(([file, alt]) => ({
      src: projectAsset('ecommerce', `${file}.webp`),
      srcSet: `${projectAsset('ecommerce', `${file}-480.webp`)} 480w, ${projectAsset('ecommerce', `${file}.webp`)} 960w`,
      width: 960,
      height: 2137,
      alt,
    })),
    note: 'Demo boundary: data and accounts are local to the device; checkout does not execute a real payment or remote order.',
  },
  {
    slug: 'instagram-clone',
    name: 'Instagram Clone',
    title: 'Instagram-inspired Social Application',
    category: 'Social Media Application',
    summary:
      'An educational Flutter and Firebase project covering posts, reels, stories, profiles, discovery, and direct conversation flows.',
    overview: [
      'This independent project uses a familiar social-media interaction model to demonstrate media handling, real-time backend integration, state management, and layered Flutter development.',
      'The repository includes Firebase-backed accounts and social content plus a separate seeded, in-memory offline demo. The demo state resets between sessions.',
    ],
    featured: false,
    status: 'Independent educational project',
    labels: [],
    stack: [
      'Flutter',
      'BLoC',
      'Firebase',
      'Cloud Firestore',
      'Firebase Storage',
      'GetIt',
    ],
    highlights: [
      'Implements email/password accounts, profiles, follows, feed posts, likes, and comments.',
      'Handles image and video media for posts, reels, and stories.',
      'Supports discovery, direct chat, and story-reply flows in the Firebase application path.',
      'Separates data sources, repositories, domain entities, BLoCs, and views.',
      'Includes committed Firestore and Storage security rules.',
    ],
    architecture:
      'Layered data/domain/view structure with BLoC and GetIt, alongside a small set of legacy paths.',
    repository: 'https://github.com/noaman03/instagram-clone',
    apkUrl:
      'https://github.com/noaman03/instagram-clone/releases/download/v1.0.0-demo.1/Instagram-Clone-v1.0.0-demo.1.apk',
    thumbnail: {
      src: projectAsset('instagram-clone', 'thumbnail.webp'),
      srcSet: `${projectAsset('instagram-clone', 'thumbnail-640.webp')} 640w, ${projectAsset('instagram-clone', 'thumbnail.webp')} 1200w`,
      width: 1200,
      height: 675,
      alt: 'Instagram-inspired Flutter feed shown in a neutral social application cover.',
    },
    gallery: [
      [
        'instagram-splash',
        'Opening screen of the independent Instagram-inspired Flutter project.',
      ],
      [
        'instagram-login',
        'Email and password sign-in screen for the social application.',
      ],
      [
        'instagram-signup',
        'Account registration screen for the social application.',
      ],
      [
        'instagram-home-feed',
        'Social feed with story and post components in the Flutter application.',
      ],
    ].map(([file, alt]) => ({
      src: projectAsset('instagram-clone', `${file}.webp`),
      srcSet: `${projectAsset('instagram-clone', `${file}-480.webp`)} 480w, ${projectAsset('instagram-clone', `${file}.webp`)} 960w`,
      width: 960,
      height: 2137,
      alt,
    })),
    disclaimer:
      'Independent educational project; not affiliated with Instagram or Meta.',
    note: 'A demo APK and a walkthrough video are published with the GitHub release. The offline demo mode works without any backend.',
  },
  {
    slug: 'food-delivery-ui',
    name: 'Food Delivery Application — UI Only',
    title: 'Food Delivery — Flutter UI Concept',
    category: 'Flutter UI Concept',
    summary:
      'A Flutter food-delivery interface focused on responsive layouts, reusable components, navigation, and a polished local checkout journey.',
    overview: [
      'This UI-only project demonstrates how a food ordering experience can be structured across discovery, cart, checkout, map selection, and order-status screens.',
      'All catalogue, transaction, and order behavior is local or simulated. There is no connected authentication, backend, order persistence, real payment, routing service, or driver tracking.',
    ],
    featured: false,
    status: 'UI-only project',
    labels: ['UI-Only Project'],
    stack: ['Flutter', 'Dart', 'GetX', 'flutter_map', 'OpenStreetMap'],
    highlights: [
      'Builds responsive discovery, basket, checkout, and order-status interfaces.',
      'Uses reusable widgets and GetX navigation/state for local demonstration flows.',
      'Supports tap-to-select map interactions with local distance and fee calculation.',
      'Organizes selected features into data, domain, and presentation boundaries.',
    ],
    architecture:
      'A selectively feature-based Flutter structure with GetX and layered boundaries in key UI flows.',
    repository: 'https://github.com/noaman03/food-delivery-app',
    apkUrl:
      'https://github.com/noaman03/food-delivery-app/releases/download/v1.0.0-demo.1/Food-Delivery-v1.0.0-demo.1.apk',
    thumbnail: {
      src: projectAsset('food-delivery-ui', 'thumbnail.webp'),
      srcSet: `${projectAsset('food-delivery-ui', 'thumbnail-640.webp')} 640w, ${projectAsset('food-delivery-ui', 'thumbnail.webp')} 1200w`,
      width: 1200,
      height: 675,
      alt: 'Food delivery Flutter UI showing the offers and restaurant discovery screen.',
    },
    gallery: [
      [
        'food-delivery-home',
        'Food delivery offers and restaurant discovery screen.',
      ],
      [
        'food-delivery-basket',
        'Food delivery basket with item quantities and order summary.',
      ],
      [
        'food-delivery-checkout',
        'Food delivery checkout and payment-method interface.',
      ],
      [
        'food-delivery-orders',
        'Food delivery active and recent order interface.',
      ],
    ].map(([file, alt]) => ({
      src: projectAsset('food-delivery-ui', `${file}.webp`),
      width: 480,
      height: 1015,
      alt,
    })),
    note: 'The supplied directory includes a demo video, but the project manifest marks the video path as unavailable; it is therefore not published.',
  },
  {
    slug: 'todo',
    name: 'Todo Application',
    title: 'Todo and Weather — Offline Productivity Application',
    category: 'Productivity Application',
    summary:
      'A compact Flutter task manager with SQLite persistence, due dates, calendar views, local reminders, and weather integration code.',
    overview: [
      'This supporting project focuses on everyday application fundamentals: task CRUD, local storage, due-date selection, calendar presentation, and scheduled local notifications.',
      'The weather request path uses device location and OpenWeatherMap, but the public repository intentionally leaves its API key blank. Weather is therefore not functional from a clean clone without configuration.',
    ],
    featured: false,
    status: 'Supporting project',
    labels: [],
    stack: [
      'Flutter',
      'Provider',
      'SQLite',
      'Geolocator',
      'HTTP',
      'TableCalendar',
    ],
    highlights: [
      'Persists task CRUD data locally with SQLite.',
      'Coordinates task state through Provider and ChangeNotifier.',
      'Adds due dates, calendar views, and scheduled local notifications.',
      'Implements a location-aware OpenWeatherMap request path with explicit loading and error states.',
    ],
    architecture:
      'A compact models/providers/screens/services/widgets structure suited to a focused utility application.',
    repository: 'https://github.com/noaman03/todo-list-and-weather',
    apkUrl:
      'https://github.com/noaman03/todo-list-and-weather/releases/download/v1.0.0-demo.1/Todo-Weather-v1.0.0-demo.1.apk',
    thumbnail: {
      src: projectAsset('todo', 'thumbnail.webp'),
      srcSet: `${projectAsset('todo', 'thumbnail-640.webp')} 640w, ${projectAsset('todo', 'thumbnail.webp')} 1200w`,
      width: 1200,
      height: 675,
      alt: 'Todo application dark home screen with tasks and a weather summary.',
    },
    gallery: [
      ['todo-home', 'Todo application task list with a weather summary.'],
      ['todo-due-date', 'Todo application due-date selection interface.'],
      ['todo-time', 'Todo application reminder time picker.'],
      [
        'todo-calendar',
        'Todo application monthly calendar and scheduled tasks.',
      ],
    ].map(([file, alt]) => ({
      src: projectAsset('todo', `${file}.webp`),
      width: 480,
      height: 1015,
      alt,
    })),
    note: 'The supplied WebM demo is not published because its 25.7 MB source has no MP4 fallback and would add disproportionate weight to the static portfolio.',
  },
];

export const featuredProjects = projects.filter((project) => project.featured);
export const additionalProjects = projects.filter(
  (project) => !project.featured,
);

export const getProject = (slug: string) =>
  projects.find((project) => project.slug === slug);
