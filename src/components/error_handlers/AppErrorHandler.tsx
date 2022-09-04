function AppErrorHandler(): JSX.Element {
  logError();
  return (
    <h1>Something went wrong...Please reload</h1>
  );
}

function logError(): void {
  // TODO: log error to service
  return;
}

export default AppErrorHandler;