/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        // Paleta minimalista preto e branco com cinzas neutros
        black: '#000000',
        white: '#FFFFFF',
        grayLight: '#F5F5F5',   // cinza claro quase branco
        gray: '#9CA3AF',        // cinza médio
        grayDark: '#4B5563',    // cinza escuro
        primary: '#000000',     // preto puro para elementos principais
        secondary: '#FFFFFF',   // branco para fundo ou textos secundários
      },
    },
    // Opcional: define o fundo padrão como branco e texto como preto
    backgroundColor: theme => ({
      ...theme('colors'),
      page: '#FFFFFF',
    }),
    textColor: theme => ({
      ...theme('colors'),
      body: '#000000',
    }),
  },
  plugins: [],
}

