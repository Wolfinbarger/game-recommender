import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		// Enable file watching through Docker volume mounts
		watch: {
			usePolling: true
		}
	}
});
