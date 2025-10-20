function dialog_start(pywebviewIsReady) {
  if (pywebviewIsReady) {
    const outputDirInput = document.getElementById('output_path_text');
    const outputDirBrowse = document.getElementById('output_path_browse');
    outputDirBrowse.addEventListener('click', open_file_dialog_JS);

    async function open_file_dialog_JS() {
      await pywebview.api.open_file_dialog_Py() // wait for python
      if (pywebview.state.output_path == undefined) {
        console.warn("`pywebview.state.output_path` is undefined")
        return undefined
      } else if (pywebview.state.output_path == null) {
        console.warn("`pywebview.state.output_path` is null")
        return null
      }
      outputDirInput.value = pywebview.state.output_path // put the path in the input
      if (outputDirInput.value != pywebview.state.output_path) { // check if it got it or not
        console.error("`outputDirInput` didn't take `pywebview.state.output_path`")
        console.warn("`outputDirInput.value`: ", outputDirInput.value)
        console.warn("`pywebview.state.output_path`: ", pywebview.state.output_path)
      }

      if (pywebview.state.LOGGING == true) // Output if LOGGING is enabled(True).
        console.info("`pywebview.state.output_path` is ", pywebview.state.output_path)
        console.info("`open_file_dialog_JS()` has finished it's process.")
    }
  }
}
