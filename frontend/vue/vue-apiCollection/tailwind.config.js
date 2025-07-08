/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: 'hsla(160, 100%, 37%, 1)',
        primaryLight: 'hsla(160, 100%, 37%, 0.2)',
      },
    },
  },
  plugins: [],
}

