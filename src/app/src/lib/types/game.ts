/**
 * Type Definitions for Game Data
 *
 * These types define the shape of data we expect from the API.
 * TypeScript uses these to help catch errors and provide autocomplete
 * suggestions in your code editor.
 */

/**
 * Represents a single game in our database.
 *
 * This interface describes all the properties a game can have.
 * Using TypeScript interfaces helps ensure we're using the data correctly
 * throughout our application.
 */
export interface Game {
  /**
   * Unique identifier for the game (from the database)
   */
  id: number;

  /**
   * The name of the game (e.g., "Satisfactory", "Minecraft")
   */
  title: string;

  /**
   * A text description of what the game is about
   */
  description: string;

  /**
   * When the game was released (as a date string)
   */
  release_date: string;

  /**
   * The review score for the game (typically 1-10)
   */
  review_score: number;

  /**
   * Optional: Information about supported platforms
   * This will be expanded when we integrate platform data
   */
  platforms?: Platform;

  /**
   * Optional: Information about multiplayer support
   * This will be expanded when we integrate multiplayer data
   */
  multiplayer?: Multiplayer;
}

/**
 * Represents platform availability for a game.
 *
 * Each property is a boolean indicating whether the game
 * is available on that platform.
 */
export interface Platform {
  pc?: boolean;
  playstation?: boolean;
  xbox?: boolean;
  nintendo?: boolean;
  steam?: boolean;
  // ... more platforms can be added as needed
}

/**
 * Represents multiplayer information for a game.
 */
export interface Multiplayer {
  /**
   * Minimum number of players
   */
  min_players?: number;

  /**
   * Maximum number of players
   */
  max_players?: number;

  /**
   * Whether the game supports online multiplayer
   */
  online?: boolean;

  /**
   * Whether the game supports local multiplayer (same screen)
   */
  local?: boolean;
}

/**
 * Represents the response from the API when fetching games.
 *
 * The API returns an object with a 'data' array containing
 * the games for the requested page.
 */
export interface GamesApiResponse {
  /**
   * Array of games returned from the API
   */
  data: Game[];

  /**
   * Optional: Total number of games available
   * This can be used to determine if there are more pages to load
   */
  num_of_objects?: number;
}
