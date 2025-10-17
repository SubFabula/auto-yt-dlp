document.addEventListener("DOMContentLoaded", () => {
  globalThis.isOffline = false

  window.addEventListener("error", (event) => { //? To read the console, use `window.addEventListener(logType, (event) => const msg = event.message || "";);`
    const msg = event.message || "";

    if (msg.includes("CLOSING") || msg.includes("CLOSED")) {
      globalThis.isOffline = true // im not sure why but only after `console.info(`"eel.onLine()" is currently ONLINE`)` in `check_eel()` sends an io to the console, will closing the command panel exit with the website.
    }
  });

  function check_eel() {
    eel._websocket.onclose = function() {
      window.close()
    }

    if (eel.onLine()) {
      if (globalThis.isOffline) {
        console.warn(`"eel.onLine()" is currently OFFLINE`)
        console.info(globalThis.isOffline)
     } else {
        console.info(`"eel.onLine()" is currently ONLINE`)
        console.info(globalThis.isOffline)
      }
    } else {
      console.warn(`"eel.onLine()" is currently OFFLINE`)
      console.info(globalThis.isOffline)
    }
  }
  
  setInterval(() => {
      check_eel();
    }, 3000); // 3000 milliseconds -> 3 seconds
});
