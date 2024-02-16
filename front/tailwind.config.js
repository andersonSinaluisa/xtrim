/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],  
  theme: {
    extend: {
      colors:{
        primary:{
          50:"#f3e7f3",
          100:"#e2c2e2",
          200:"#d09ad0",
          300:"#bd73bd",
          400:"#ae56ae",
          500:"#9f3ea1",
          600:"#92399a",
          700:"#813291",
          800:"#722e88",
          900:"#562577"
        }
      }
    },
  },
  plugins: [],
}

