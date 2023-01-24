/** @type {import('tailwindcss').Config} */
module.exports = {
  // darkMode: 'media',
  content: [
    './app/templates/**/*.html',
    './app/static/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}