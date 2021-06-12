function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = 0;
            check = document.querySelector('#again');
            check.classList.remove("hidden")
        }

    }, 1000);
}

window.onload = function () {
    var OneMinutes = 60,
        display = document.querySelector('#time');
    startTimer(OneMinutes, display);
};

document.getElementById('#again').onclick = function (){
      startTimer(OneMinutes, display);
}
