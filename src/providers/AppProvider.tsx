import React from 'react';


function AppProvider() {
  return (
    <React.Suspense fallback={<div>Loading...</div>}>
    </React.Suspense>
  );
}

export default AppProvider;