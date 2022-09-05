import React from 'react';


function AppProvider() {
  // TODO: Add a loading component
  // TODO Add other providers
  // TODO Add routing
  return (
    <React.Suspense fallback={<div>Loading...</div>}>
      
    </React.Suspense>
  );
}

export default AppProvider;