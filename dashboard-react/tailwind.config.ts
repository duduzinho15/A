/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                background: "#050b15",
                surface: "#0a1220",
                neonCyan: "#00f3ff",
                neonGreen: "#39ff14",
                neonBlue: "#0047ff",
            },
        },
    },
    plugins: [],
}
