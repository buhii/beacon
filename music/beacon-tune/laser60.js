// laser60.js

inlets = 2;
outlets = 62;
array = [59];
pattern = 0;
outFlag = true;
tick = 0;

function laserOn(x)
{
	outFlag = true;
}
function laserOff(x)
{
	outFlag = false;
}


function msg_int(a)
{
	tick = 0;
	for (var i = 0; i <= 59; i++)
	{
		outlet(i, 0);
	}
	
	pattern = a;
	if (pattern == 0)
		array = [59];
	else { if (pattern == 1)
		array = [59, 29];
	else { if (pattern == 2)
		array = [59, 19, 39];
	else { if (pattern == 3)
		array = [59, 14, 29, 44];
	}}}
}

function bang()
{
	for (var i = 0; i <= pattern; i++)
	{
		tmp = (60 + array[i]) % 60;
		/*if (outFlag == true) */ 
		outlet(conv(tmp), 0);
		array[i] = (array[i] + 1) % 60;
		if (outFlag == true) outlet(conv(array[i]), 1);
	}
	for (var i = 0; i <= pattern; i++) 
	{
		outlet(60, array[i]);
	}
	
	// count tick
	outlet(61, tick);
	tick++;
}

function conv(num) {
	if (num > 44) {
		num -= 45;
	} else {
		if (num > 29) {
			num -= 15;
		} else {
			if (num > 14) {
				num += 15;
			} else {
				if (num > -1) {
					num += 45;
				}
			}
		}
	}
	return num;
}
