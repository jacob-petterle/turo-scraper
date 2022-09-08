import React from 'react';
import { MainLayout } from '../components/layout/MainLayout';


function AppProvider() {
  // TODO: Add a loading component
  // TODO Add other providers
  // TODO Add routing
  return (
    <React.Suspense fallback={<div>Loading...</div>}>
      <MainLayout>
        <div>Content</div>
      </MainLayout>
    </React.Suspense>
  );
}

export default AppProvider;