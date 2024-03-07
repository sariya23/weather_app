function disableButtonWithEmtyInput() {
    const sendCity = document.getElementById("sendCity");
    const cityInput = document.getElementById("floatingInput");

    cityInput.oninput = function () {
        if (cityInput.value.length === 0) {
            sendCity.disabled = true;
        } else {
            sendCity.disabled = false;
        }
    }
}