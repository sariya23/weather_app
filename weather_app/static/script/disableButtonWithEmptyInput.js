const sendCity = document.getElementById("sendCity");
const cityInput = document.getElementById("cityInput");

cityInput.oninput = function () {
    if (cityInput.value.trim().length === 0) {
        sendCity.disabled = true;
    } else {
        sendCity.disabled = false;
    }
}
