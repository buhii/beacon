inlets = 1;
outlets = 3;
tune_mode = 0;
old_num = 999;
tune = new Array(2);

LASEROFF  = 4398764;
LASERON   = 6983059;
TUNEEND	  = 5498725;
NO_NOTE	  = 36660;

now_note = NO_NOTE;


/* -------------------------------------*/
/*                void                  */
/* -------------------------------------*/

tune[0] = [
	[999,999,999, LASEROFF ],
	[999,999,999, 999],
	[999,999,999, 33],
	[999,999,999, 999],
	[999,999,999, 33],
	[999,999,999, 999],
	];

/* -------------------------------------*/
/*   orpheus in the underworld - Galop  */
/* -------------------------------------*/

tune[1] = [
	[999,999,999, LASEROFF],
	[999,999,999, 999],
	[999,999,999, 33],
	[999,999,999, 33],
	[999,999,999, 33],
	[999,999,999, 33],

	[62, 64, 66, LASERON],
	[999, 999, 999, 999],
	[64, 67, 69, 999],
	[64, 66, 68, 999],
	[65, 67, 69, 999],
	[65, 67, 69, 999],
	[67, 69, 71, 999],
	[66, 67, 69, 999],
	[62, 64, 66, 999],
	[62, 64, 66, 999],
	[64, 67, 69, 999],
	[64, 66, 68, 999],
	[62, 68, 74, 999],
	[69, 71, 73, 999],
	[65, 67, 69, 999],
	[64, 66, 68, 999],
	[62, 64, 66, 999],
	[999, 999, 999, 999],
	[64, 67, 69, 999],
	[64, 66, 68, 999],
	[65, 67, 69, 999],
	[65, 67, 69, 999],
	[67, 69, 71, 999],
	[66, 67, 69, 999],
	[62, 64, 66, 999],
	[62, 64, 66, 999],
	[64, 67, 69, 999],
	[64, 66, 68, 999],
	[70, 72, 74, 999],
	[62, 64, 66, 999],
	[62, 64, 66, 999],
	[64, 66, 68, 999],
	[65, 67, 69, 999],
	[69, 71, 73, 999],
	[69, 74, 79, 999],
	[74, 76, 78, 999],
	[70, 72, 74, 999],
	[62, 64, 66, 999],
	[62, 64, 66, 999],
	[64, 66, 68, 999],
	[65, 67, 69, 999],
	[69, 71, 73, 999],
	[69, 74, 79, 999],
	[74, 76, 78, 999],
	[70, 72, 74, 999],
	[70, 72, 74, 999],
	[74, 76, 78, 999],
	[74, 76, 78, 999],
	[70, 72, 74, 999],
	[70, 72, 74, 999],
	[74, 76, 78, 999],
	[74, 76, 78, 999],
	[70, 72, 74, 999],
	[70, 72, 74, 999],
	[70, 72, 74, 999],
	[70, 72, 74, 999],
	[62, 64, 66, 999],
	[62, 64, 66, 999],
	];

/* -------------------------------------*/
/*               function               */
/* -------------------------------------*/
function setFlag(x)
{
	outlet(2, x);
}

function list(a)
{
	cmt = arguments[0];		// Chikai Man-naka Toi :-)
	num = arguments[1];		// tick
	ac  = tune[tune_mode][num][3];	// accompaniment with flag

	// output Off
	if (num == (tune[tune_mode].length - 1) ) { setFlag(TUNEEND); }

	// output accompaniment, flag
	if (old_num != num) {
		switch (ac) {
		case LASEROFF: 	setFlag(LASEROFF); break;
		case LASERON: 	setFlag(LASERON); cmt = -1; break;
		case 999:	break;
		default:	outlet(1, ac);	// accompaniment
		}
	}
	old_num = num;

	// output tune
	if (cmt == -1) {
		if (now_note != NO_NOTE) {
			outlet(0, [now_note, 0]);	// note off
			now_note = NO_NOTE;
		}
		flag_con = true;
	} else {
		if (flag_con == true)
		{
			if (tune[tune_mode][num][cmt] != 999) {
				now_note = tune[tune_mode][num][cmt];
				outlet(0, [now_note, 127]);	// note on
			}
		}
		flag_con = false;
	}
}

function msg_int(x)
{
	if (x == 1) { post("Tune\n"); tune_mode = 1; old_num = 999; return; }
	if (x == 3) { post("Void\n"); tune_mode = 0; old_num = 999; return; }
}
