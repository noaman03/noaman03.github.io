import eslint from '@eslint/js';
import astro from 'eslint-plugin-astro';

export default [
  {
    ignores: ['.astro/**', 'dist/**', 'node_modules/**', 'public/**', 'tmp/**'],
  },
  eslint.configs.recommended,
  ...astro.configs.recommended,
  {
    files: ['scripts/**/*.mjs', '*.config.js', '*.config.mjs'],
    languageOptions: {
      globals: {
        console: 'readonly',
        process: 'readonly',
      },
    },
  },
  {
    rules: {
      'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    },
  },
];
