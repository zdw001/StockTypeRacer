function Stopwatch() {
	var  time = 0;
	var interval;
	var offset;

	function update() {
		time += delta();
		var formattedTime = timeFormatter(time);
		document.getElementById("timer").innerHTML = formattedTime;
		// var wpm = wordsPerMinute(time, wordsCorrect)
		return time;
	};

	function delta() {
		var now = Date.now()
		var timePassed = now - offset;
		offset = now;
		return timePassed;
	};

	function pad (n) {
        return ('00' + n).substr(-2);
    }

	function timeFormatter(timeInMilliseconds) {
		var time = new Date(timeInMilliseconds);
		var minutes = pad(time.getMinutes());
		var seconds = pad(time.getSeconds());
		var milliseconds = pad(Math.floor(time.getMilliseconds()/10));

		return minutes + " : " + seconds + ' : ' + milliseconds;

	};

	function wordsPerMinute(timeInMilliseconds, wordsCorrect) {
		var wpm = wordsCorrect/(timeInMilliseconds/(60*1000));
		return wpm;
	}
 

	this.isOn = false;
	this.start = function() {
		if (!this.isOn) {
			interval = setInterval(update, 10);
			offset = Date.now();
			this.isOn = true;
		}
	};

	this.stop = function() {
		if (this.isOn) {
			clearInterval(interval);
			interval = null;
			this.isOn = false;
		}
	};

	this.time = function () {
		return time;
	}

}