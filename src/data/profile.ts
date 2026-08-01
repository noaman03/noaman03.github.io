export const profile = {
  name: 'Ahmed Mohamed Noaman',
  shortName: 'Ahmed Noaman',
  title: 'Flutter Developer & Mobile Application Engineer',
  location: 'Alexandria, Egypt',
  email: 'noamana455@gmail.com',
  github: 'https://github.com/noaman03',
  linkedin: 'https://www.linkedin.com/in/ahmed-noaman-07ab162b4',
  site: 'https://noaman03.github.io',
  cv: '/documents/Ahmed-Mohamed-Noaman-CV.pdf',
} as const;

export const expertise = [
  {
    title: 'Mobile development',
    accent: true,
    skills: [
      'Flutter',
      'Dart',
      'Swift',
      'Native platform integration',
      'Responsive UI',
      'Reusable widgets',
    ],
  },
  {
    title: 'Architecture',
    accent: true,
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
    accent: true,
    skills: ['Riverpod', 'BLoC', 'Cubit', 'Provider', 'GetX'],
  },
  {
    title: 'Backend and data',
    accent: false,
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
    accent: false,
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
    accent: false,
    skills: [
      'YOLOv8',
      'Computer vision',
      'Web3dart',
      'Blockchain integration',
      'Real-time communications',
    ],
  },
  {
    title: 'Engineering tools',
    accent: false,
    skills: [
      'Git',
      'GitHub',
      'Postman',
      'CI/CD',
      'Testing',
      'Quality assurance',
    ],
  },
  {
    title: 'Security and networking',
    accent: false,
    skills: [
      'Cisco CyberOps',
      'CCNA',
      'Identity and Access Management',
      'Secure-by-design development',
    ],
  },
] as const;

export const certifications = [
  'Flutter Diploma — AMIT Learning — Grade 95%',
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
