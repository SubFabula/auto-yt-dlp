window.addEventListener('pywebviewready', () => { // wait for pywebview
  while (pywebview.api.echo == undefined) { // and check it
    console.warn("`pywebview.api.` haven't loaded!")
  }

  pywebview.api.echo() // call if pywebview is ready/available

  globalThis.pywebviewIsReady = true
  dialog_start(pywebviewIsReady)
});
