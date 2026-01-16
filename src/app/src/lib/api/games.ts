/**
 * API Client for Game Data
 *
 * This file contains functions that communicate with our backend API
 * to fetch game data. By centralizing API calls here, we can:
 * 1. Reuse the same code across different components
 * 2. Handle errors in a consistent way
 * 3. Easily update the API endpoint if it changes
 */

import { PUBLIC_API_URL } from '$env/static/public';
import type { GamesApiResponse } from '$lib/types/game';

/**
 * The base URL for our backend API.
 *
 * This is read from the PUBLIC_API_URL environment variable, which allows
 * the app to work in different environments:
 * - Local development: http://127.0.0.1:8000 (or localhost:8000)
 * - Docker: http://backend:8000 (using Docker service name)
 * - Production: Your deployed backend URL
 *
 * The environment variable is set in:
 * - Local: .env file in src/app/
 * - Docker: compose.yaml file
 */
const BASE_URL = `${PUBLIC_API_URL}/api/games`;

/**
 * Fetches a page of games from the backend API.
 *
 * This function makes an HTTP request to our FastAPI backend
 * and returns the game data for the requested page.
 *
 * @param pageNumber - The page number to fetch (starts at 1)
 * @returns A promise that resolves to the games data
 * @throws Error if the API request fails
 *
 * @example
 * ```typescript
 * // Fetch the first page of games
 * const games = await fetchGames(1);
 * console.log(games.data); // Array of game objects
 * ```
 */
export async function fetchGames(pageNumber: number): Promise<GamesApiResponse> {
  try {
    // Make the HTTP GET request to the API
    // The ?page_number= query parameter tells the API which page we want
    const response = await fetch(`${BASE_URL}?page_number=${pageNumber}`);

    // Check if the request was successful
    // HTTP status codes in the 200-299 range indicate success
    if (!response.ok) {
      throw new Error(`HTTP error: The status is ${response.status}`);
    }

    // Parse the JSON response from the API
    // This converts the text response into a JavaScript object
    const data: GamesApiResponse = await response.json();

    return data;
  } catch (error) {
    // If anything goes wrong (network error, bad response, etc.),
    // we throw a new error with a helpful message
    console.error('Error fetching games:', error);
    throw new Error(
      `Failed to fetch games: ${error instanceof Error ? error.message : 'Unknown error'}`
    );
  }
}
