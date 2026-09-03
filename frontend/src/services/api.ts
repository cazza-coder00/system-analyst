// frontend/src/services/api.ts

import axios from 'axios';

// Configura a URL base do nosso back-end FastAPI que roda na porta 8000
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;