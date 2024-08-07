import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    assetsDir: "./production",
  },
  // Explicitly tell the server to use 127.0.0.1 instead of localhost to resolve a CORS issue where Django doesn't
  // recognize localhost.
  server: {
    host: "0.0.0.0",
    port: 5173,
  },
});
