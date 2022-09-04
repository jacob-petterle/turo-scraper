import React from 'react';
import { ErrorBoundary } from 'react-error-boundary';
import ReactDOM from 'react-dom/client';
import './components/styles/index.css';
import reportWebVitals from './reportWebVitals';


import App from './App';
import AppErrorHandler from './components/error_handlers/AppErrorHandler';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <ErrorBoundary FallbackComponent={AppErrorHandler}>
      <App />
    </ErrorBoundary>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
