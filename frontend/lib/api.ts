// Centralized API configuration

const BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const API_CONFIG = {
  BASE_URL,
  ENDPOINTS: {
    TASKS: `${BASE_URL}/api/tasks`
  },
  
  // HTTP client configuration
  DEFAULT_HEADERS: {
    'Content-Type': 'application/json',
  },
  
  // Environment info
  IS_DEVELOPMENT: process.env.NEXT_PUBLIC_ENV === 'development',
  IS_PRODUCTION: process.env.NEXT_PUBLIC_ENV === 'production',
};

export const ENDPOINTS = API_CONFIG.ENDPOINTS;

// Debug logging for development
if (API_CONFIG.IS_DEVELOPMENT) {
  console.log('API Configuration:', {
    BASE_URL: API_CONFIG.BASE_URL,
    ENDPOINTS: API_CONFIG.ENDPOINTS,
    ENV: process.env.NEXT_PUBLIC_ENV
  });
}