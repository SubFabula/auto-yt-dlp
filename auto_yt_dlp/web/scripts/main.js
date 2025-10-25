import * as utils from "./utils.js";

window.addEventListener('pywebviewready', () => { // wait for pywebview
  console.debug("`'pywebviewready', () => {}` has been called!")

  while (pywebview.api == undefined) { // and check it
    console.warn("`pywebview` haven't loaded for JS!")
    globalThis.pywebviewIsReady = false
  }

  pywebview.api.echo() // call if pywebview is ready/available

  globalThis.pywebviewIsReady = true

  // Do the same logger set up from the Python side
  console.info("`pywebview.state.DEBUG` =", pywebview.state.DEBUG)
  console.info("`pywebview.state.LOGGING` =", pywebview.state.LOGGING)

  const DEBUG = pywebview.state.DEBUG
  const LOGGING = pywebview.state.LOGGING

  if (LOGGING === false) {
    setTimeout(() => {
      console.log = function () {}
      console.debug = function () {}
      console.info = function () {}
      console.warn = function () {}
    }, 1500) // 1,5sec
  }

  document.addEventListener('DOMContentLoaded', console.debug("`DOMContentLoaded` is loaded!")) // checking just in case

  console.debug("`'pywebviewready', () => {}` has been set!")
});

document.addEventListener('DOMContentLoaded', async () => {
  console.debug("`'DOMContentLoaded', () => {}` has been called!")

  async function checkThis() { // check if pywebview is defined from here
    console.debug("checking `globalThis.pywebviewIsReady`...")
    if (!globalThis.pywebviewIsReady) {
      console.debug("`globalThis.pywebviewIsReady` is", globalThis.pywebviewIsReady)
      await new Promise((resolve) => { {
        const awaitThis = setInterval(() => {
          console.debug("checking again...")
          if (!globalThis.pywebviewIsReady) {
            console.debug("`globalThis.pywebviewIsReady` is", globalThis.pywebviewIsReady)
          } else {
            clearInterval(awaitThis)
            console.debug("`globalThis.pywebviewIsReady` is", globalThis.pywebviewIsReady)
            resolve()
          }
        }, 1000); // 1sec
      }})
    }
  }

  await checkThis()

  // Path\Name Output
  const outputDirectInput = document.getElementById('output_path_text');
  const outputDirectBrowse = document.getElementById('output_path_browse');
  // URL Input
  const inputURL = document.getElementById('url-input');
  // Command Prompt Viewer
  const CMDviewer = document.getElementById('command_view_text');
  const CMDrun = document.getElementById('command_view_run'); // Input[Button] of `#command_run` Label
  const CMDrunStyle = document.getElementById('command_run'); // Label of `#command_view_run` Input[Button]
  const CMDoutput = document.getElementById('command_output_text');
  const CMDoutputH1 = document.getElementById('command_output-h1');

  outputDirectInput.addEventListener('keyup', () => utils.update_oPathCMDview(CMDviewer, outputDirectInput));
  outputDirectBrowse.addEventListener('click', () => utils.open_file_dialog(outputDirectInput, CMDviewer));
  inputURL.addEventListener('keyup', () => utils.update_URLCMDview(CMDviewer, inputURL, utils.oPathEndIndex_CMDviewer));
  CMDrun.addEventListener('click', () => utils.runCMD(CMDviewer, CMDrun, CMDrunStyle, CMDoutput, CMDoutputH1));

  utils.update_oPathCMDview(CMDviewer, outputDirectInput) // running it once to set some variables

  console.debug("`'DOMContentLoaded', () => {}` has been set!")
});