export async function open_file_dialog(outputDirectInput, CMDviewer) {
  console.debug("`open_file_dialog` has been called!")
  await pywebview.api.open_file_dialog() // wait for python
  const output_path = pywebview.state.output_path.replace(/\//g, "\\") + '\\%(title)s.%(ext)s'

  outputDirectInput.value = output_path // put the path in the input
  if (outputDirectInput.value != output_path) { // and check if it got it or not
    console.error("`outputDirectInput` didn't take `pywebview.state.output_path`")
    console.debug("`outputDirectInput.value` =", outputDirectInput.value)
    console.debug("`output_path` =", output_path)
    console.debug("`pywebview.state.output_path` =", pywebview.state.output_path)
  }

  console.debug("`pywebview.state.output_path` is", pywebview.state.output_path)
  console.debug("`open_file_dialog()` has ended and calling `update_oPathCMDview()`!")
  update_oPathCMDview(CMDviewer, outputDirectInput)
}

export let oPathEndIndex_CMDviewer = Number

export async function update_oPathCMDview(CMDviewer, outputDirectInput) { // Update `-o [PATH]` in the Command View
  console.debug("`update_oPathCMDview()` has been called!")

  outputDirectInput.value = outputDirectInput.value.replace(/\//g, "\\")

  let oIndex_CMDviewer = CMDviewer.value.indexOf('-o')
  let oPathIndex_CMDviewer = oIndex_CMDviewer + 4
  oPathEndIndex_CMDviewer = CMDviewer.value.indexOf('"', oPathIndex_CMDviewer)

  if (!outputDirectInput.value) {
    CMDviewer.value = CMDviewer.value.slice(0, oPathIndex_CMDviewer) + '%USERPROFILE%\\ThankYouForTesting.%(ext)s' + CMDviewer.value.slice(oPathEndIndex_CMDviewer, CMDviewer.length)
  } else {
    CMDviewer.value = CMDviewer.value.slice(0, oPathIndex_CMDviewer) + outputDirectInput.value + CMDviewer.value.slice(oPathEndIndex_CMDviewer, CMDviewer.length)
  }

  oIndex_CMDviewer = CMDviewer.value.indexOf('-o')
  oPathIndex_CMDviewer = oIndex_CMDviewer + 4
  oPathEndIndex_CMDviewer = CMDviewer.value.indexOf('"', oPathIndex_CMDviewer)

  console.debug("`oIndex_CMDviewer` =", oIndex_CMDviewer)
  console.debug("`oPathIndex_CMDviewer` =", oPathIndex_CMDviewer)
  console.debug("`oPathEndIndex_CMDviewer` =", oPathEndIndex_CMDviewer)

  console.debug("`outputDirectInput.value` =", outputDirectInput.value)

  console.debug("`update_oPathCMDview()` has ended!")
}

export async function update_URLCMDview(CMDviewer, inputURL, oPathEndIndex_CMDviewer) { // Update `[URL]` in the Command View
  console.debug("`update_URLCMDview()` has been called!")

  let URLIndex_CMDviewer = oPathEndIndex_CMDviewer + 3
  let URLEndIndex_CMDviewer = CMDviewer.value.indexOf('"', URLIndex_CMDviewer)
  
  if (!inputURL.value) {
    CMDviewer.value = CMDviewer.value.slice(0, URLIndex_CMDviewer) + 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' + CMDviewer.value.slice(URLEndIndex_CMDviewer, CMDviewer.length)
  } else {
    CMDviewer.value = CMDviewer.value.slice(0, URLIndex_CMDviewer) + inputURL.value + CMDviewer.value.slice(URLEndIndex_CMDviewer, CMDviewer.length)
  }

  URLIndex_CMDviewer = oPathEndIndex_CMDviewer + 3
  URLEndIndex_CMDviewer = CMDviewer.value.indexOf('"', URLIndex_CMDviewer)

  console.debug("`URLIndex_CMDviewer` =", URLIndex_CMDviewer)
  console.debug("`URLEndIndex_CMDviewer` =", URLEndIndex_CMDviewer)

  console.debug("`inputURL.value` =", inputURL.value)

  console.debug("`update_URLCMDview()` has ended!")
}

async function runCMD_await(CMDrun, CMDrunStyle) {
  console.debug("`runCMD_await()` has been called!")

  console.debug("`pywebview.state.runCMD_isRunning` is ", pywebview.state.runCMD_isRunning)
  console.debug("`CMDrun.dataset.running` is ", CMDrun.dataset.running)

  CMDrunStyle.innerText = 'Stop Downloading | Downloading';
  
  await new Promise((resolve) => {
    const animation = setInterval(() => {
      console.debug("`Downloading...` animation playing...")
      console.debug("`CMDrunStyle.innerText` is ", CMDrunStyle.innerText)
      if (CMDrunStyle.innerText == 'Stop Downloading | Downloading...') {
        CMDrunStyle.innerText = 'Stop Downloading | Downloading';
      }

      CMDrunStyle.innerText += '.'

      if (!pywebview.state.runCMD_isRunning || CMDrun.dataset.running == "false") {
        console.debug("`Downloading...` animation stopping...")
        clearInterval(animation)
        console.debug("resolve")
        resolve
      }
    }, 2000); // 2sec
    
  })

  CMDrunStyle.innerText = 'Download the Audio/Video File';

  console.debug("`pywebview.state.runCMD_isRunning` is ", pywebview.state.runCMD_isRunning)
  console.debug("`CMDrun.dataset.running` is ", CMDrun.dataset.running)

  console.debug("`runCMD_await()` has ended!")
}

async function runCMD_clear(clear_CMDoutput, c_CMDo, openDownload, CMDoutput, CMDoutputH1) {
  console.debug("`runCMD_clear()` has been called!")

  clear_CMDoutput.style.display = 'block';
  openDownload.style.display = 'block';

  await c_CMDo

  CMDoutput.value = '';
  CMDoutput.display = 'none';
  CMDoutputH1.display = 'none';

  clear_CMDoutput.style.display = 'none';
  openDownload.style.display = 'none';

  console.debug("`runCMD_clear()` has ended!")
}

export async function runCMD(CMDviewer, CMDrun, CMDrunStyle, CMDoutput, CMDoutputH1, clear_CMDoutput, c_CMDo, openDownload) {
  console.debug("`runCMD()` has been called!")

  CMDoutputH1.style.display = 'block';
  CMDoutput.style.display = 'block';

  CMDrunStyle.style.backgroundColor = 'Gray';
  CMDrunStyle.style.borderColor = 'Gray';

  pywebview.api.runCMD(CMDviewer.value)

  CMDrun.dataset.running = "true";

  console.debug("`runCMD()` is calling `runCMD_await()`!")

  await runCMD_await(CMDrun, CMDrunStyle)

  CMDrunStyle.style.display = 'none';
  CMDrunStyle.style.backgroundColor = 'Red';
  CMDrunStyle.style.borderColor = 'Red';

  console.debug("`runCMD()` is calling `runCMD_clear()`!")

  await runCMD_clear(clear_CMDoutput, c_CMDo, openDownload, CMDoutput, CMDoutputH1)

  CMDrun.dataset.running = "false";
  CMDrunStyle.style.display = 'inline-block';

  console.debug("`runCMD()` has ended!")
}

export function openDownload_sDirect(outputDirectInput) {
  let path = '%USERPROFILE%\\'
  
  if (outputDirectInput.value) {
    if (outputDirectInput.value.search("%(title)s") || outputDirectInput.value.search("%(ext)s")) {
      path = outputDirectInput.value.substring(0, outputDirectInput.value.lastIndexOf("\\") + 1)
      pywebview.state.isItFolder = true
    } else {
      path = outputDirectInput.value
      pywebview.state.isItFolder = false
    }
  }

  console.debug("`path` = ", path)
  pywebview.api.openDownload_sDirect(path)
}

/*
let jsLineOpen = '[Merger] Merging formats into \"C:\\Users\\USERNAME\\ThankYouForTesting.webm\"\n'
let jsLO_Merger_rfind = jsLineOpen.lastIndexOf('[Merger]')
let jsLO_MergerExtensionStart_rfind = jsLineOpen.lastIndexOf('.', jsLO_Merger_rfind)
let jsLO_MergerExtensionEnd_find = jsLineOpen.indexOf('/\/', jsLO_MergerExtensionStart_rfind)
let path = jsLineOpen.substring(jsLO_MergerExtensionStart_rfind, jsLO_MergerExtensionEnd_find)

document.getElementById("demo").innerHTML = path;
*/