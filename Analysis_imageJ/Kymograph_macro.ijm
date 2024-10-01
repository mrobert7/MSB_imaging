dir_well1_white = getDirectory("Choose Source Directory well1_white");
dir_well1_blue = getDirectory("Choose Source Directory well1_blue");
dir_well1_green = getDirectory("Choose Source Directory well1_green");
dir_well2_white = getDirectory("Choose Source Directory well2_white");
dir_well2_blue = getDirectory("Choose Source Directory well2_blue");
dir_well2_green = getDirectory("Choose Source Directory well2_green");
dir_well3_white = getDirectory("Choose Source Directory well3_white");
dir_well3_blue = getDirectory("Choose Source Directory well3_blue");
dir_well3_green = getDirectory("Choose Source Directory well3_green");
dir_well4_white = getDirectory("Choose Source Directory well4_white");
dir_well4_blue = getDirectory("Choose Source Directory well4_blue");
dir_well4_green = getDirectory("Choose Source Directory well4_green");
dir_well5_white = getDirectory("Choose Source Directory well5_white");
dir_well5_blue = getDirectory("Choose Source Directory well5_blue");
dir_well5_green = getDirectory("Choose Source Directory well5_green");
dir_well6_white = getDirectory("Choose Source Directory well6_white");
dir_well6_blue = getDirectory("Choose Source Directory well6_blue");
dir_well6_green = getDirectory("Choose Source Directory well6_green");
dir_well7_white = getDirectory("Choose Source Directory well7_white");
dir_well7_blue = getDirectory("Choose Source Directory well7_blue");
dir_well7_green = getDirectory("Choose Source Directory well7_green");
dir_well8_white = getDirectory("Choose Source Directory well8_white");
dir_well8_blue = getDirectory("Choose Source Directory well8_blue");
dir_well8_green = getDirectory("Choose Source Directory wel8_green");
dir_well9_white = getDirectory("Choose Source Directory well9_white");
dir_well9_blue = getDirectory("Choose Source Directory well9_blue");
dir_well9_green = getDirectory("Choose Source Directory well9_green");




list_well1_white = getFileList(dir_well1_white);
list_well1_blue = getFileList(dir_well1_blue);
list_well1_green = getFileList(dir_well1_green);
list_well2_white = getFileList(dir_well2_white);
list_well2_blue = getFileList(dir_well2_blue);
list_well2_green = getFileList(dir_well2_green);
list_well3_white = getFileList(dir_well3_white);
list_well3_blue = getFileList(dir_well3_blue);
list_well3_green = getFileList(dir_well3_green);
list_well4_white = getFileList(dir_well4_white);
list_well4_blue = getFileList(dir_well4_blue);
list_well4_green = getFileList(dir_well4_green);
list_well5_white = getFileList(dir_well5_white);
list_well5_blue = getFileList(dir_well5_blue);
list_well5_green = getFileList(dir_well5_green);
list_well6_white = getFileList(dir_well6_white);
list_well6_blue = getFileList(dir_well6_blue);
list_well6_green = getFileList(dir_well6_green);
list_well7_white = getFileList(dir_well7_white);
list_well7_blue = getFileList(dir_well7_blue);
list_well7_green = getFileList(dir_well7_green);
list_well8_white = getFileList(dir_well8_white);
list_well8_blue = getFileList(dir_well8_blue);
list_well8_green = getFileList(dir_well8_green);
list_well9_white = getFileList(dir_well9_white);
list_well9_blue = getFileList(dir_well9_blue);
list_well9_green = getFileList(dir_well9_green);


// well1_測定座標
x1_well1 = 1026;  // x1の値
y1_well1 = 631;    // y1の値
x2_well1 = 1026; // x2の値
y2_well1 = 1165; // y2の値

// well2_測定座標
x1_well2 = 1060;  // x1の値
y1_well2 = 645;    // y1の値
x2_well2 = 1060; // x2の値
y2_well2 = 1179; // y2の値

// well3_測定座標
x1_well3 = 1066;  // x1の値
y1_well3 = 636;    // y1の値
x2_well3 = 1066; // x2の値
y2_well3 = 1170; // y2の値

// well4_測定座標
x1_well4 = 1051;  // x1の値
y1_well4 = 630;    // y1の値
x2_well4 = 1051; // x2の値
y2_well4 = 1164; // y2の値

// well5_測標
x1_well5 = 1054;  // x1の値
y1_well5 = 636;    // y1の値
x2_well5 = 1054; // x2の値
y2_well5 = 1170; // y2の値

// well6_測定座標
x1_well6 = 1060;  // x1の値
y1_well6 = 630;    // y1の値
x2_well6 = 1060; // x2の値
y2_well6 = 1164; // y2の値

// well7_測定座標
x1_well7 = 1054;  // x1の値
y1_well7 = 633;    // y1の値
x2_well7 = 1054; // x2の値
y2_well7 = 1167; // y2の値

// well8_測定座標
x1_well8 = 1066;  // x1の値
y1_well8 = 639;    // y1の値
x2_well8 = 1066; // x2の値
y2_well8 = 1173; // y2の値

// well9_測定座標
x1_well9 = 1062;  // x1の値
y1_well9 = 651;    // y1の値
x2_well9 = 1062; // x2の値
y2_well9 = 1185; // y2の値



setBatchMode(false);

// well1
// well1_white
for (i=0; i<list_well1_white.length; i++) {
    showProgress(i+1, list_well1_white.length);
    open(dir_well1_white + list_well1_white[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    run("Invert");
    // 縦
    makeLine(x1_well1, y1_well1, x2_well1, y2_well1);
    pf = getProfile();
    Array.print(pf);
    close();
    }
    string = getInfo("Log");
    File.saveString(string, dir_well1_white + "result_well1_white" + i + ".csv");
    close("Log");

// well1_blue
for (i=0; i<list_well1_blue.length; i++) {
    showProgress(i+1, list_well1_blue.length);
    open(dir_well1_blue + list_well1_blue[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well1, y1_well1, x2_well1, y2_well1);
    pf = getProfile();
    Array.print(pf);
    close();
    }
    string = getInfo("Log");
    File.saveString(string, dir_well1_blue + "result_well1_blue" + i + ".csv");
    close("Log");
    
// well1_green
for (i=0; i<list_well1_green.length; i++) {
    showProgress(i+1, list_well1_green.length);
    open(dir_well1_green + list_well1_green[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well1, y1_well1, x2_well1, y2_well1);
    pf = getProfile();
    Array.print(pf);
    close();
    }
    string = getInfo("Log");
    File.saveString(string, dir_well1_green + "result_well1_green" + i + ".csv");
    close("Log");
    
// well2
// well2_white
for (i = 0; i < list_well2_white.length; i++) {
    showProgress(i + 1, list_well2_white.length);
    open(dir_well2_white + list_well2_white[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    run("Invert");
    // 縦
    makeLine(x1_well2, y1_well2, x2_well2, y2_well2);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well2_white + "result_well2_white" + i + ".csv");
    close("Log");


// well2_blue
for (i = 0; i < list_well2_blue.length; i++) {
    showProgress(i + 1, list_well2_blue.length);
    open(dir_well2_blue + list_well2_blue[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well2, y1_well2, x2_well2, y2_well2);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well2_blue + "result_well2_blue" + i + ".csv");
    close("Log");


// well2_green
for (i = 0; i < list_well2_green.length; i++) {
    showProgress(i + 1, list_well2_green.length);
    open(dir_well2_green + list_well2_green[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well2, y1_well2, x2_well2, y2_well2);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well2_green + "result_well2_green" + i + ".csv");
    close("Log");


// well3
// well3_white
for (i = 0; i < list_well3_white.length; i++) {
    showProgress(i + 1, list_well3_white.length);
    open(dir_well3_white + list_well3_white[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    run("Invert");
    // 縦
    makeLine(x1_well3, y1_well3, x2_well3, y2_well3);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well3_white + "result_well3_white" + i + ".csv");
    close("Log");


// well3_blue
for (i = 0; i < list_well3_blue.length; i++) {
    showProgress(i + 1, list_well3_blue.length);
    open(dir_well3_blue + list_well3_blue[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well3, y1_well3, x2_well3, y2_well3);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well3_blue + "result_well3_blue" + i + ".csv");
    close("Log");


// well3_green
for (i = 0; i < list_well3_green.length; i++) {
    showProgress(i + 1, list_well3_green.length);
    open(dir_well3_green + list_well3_green[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well3, y1_well3, x2_well3, y2_well3);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well3_green + "result_well3_green" + i + ".csv");
    close("Log");
    
// well4
// well4_white
for (i = 0; i < list_well4_white.length; i++) {
    showProgress(i + 1, list_well4_white.length);
    open(dir_well4_white + list_well4_white[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    run("Invert");
    // 縦
    makeLine(x1_well4, y1_well4, x2_well4, y2_well4);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well4_white + "result_well4_white" + i + ".csv");
    close("Log");


// well4_blue
for (i = 0; i < list_well4_blue.length; i++) {
    showProgress(i + 1, list_well4_blue.length);
    open(dir_well4_blue + list_well4_blue[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well4, y1_well4, x2_well4, y2_well4);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well4_blue + "result_well4_blue" + i + ".csv");
    close("Log");


// well4_green
for (i = 0; i < list_well4_green.length; i++) {
    showProgress(i + 1, list_well4_green.length);
    open(dir_well4_green + list_well4_green[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well4, y1_well4, x2_well4, y2_well4);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well4_green + "result_well4_green" + i + ".csv");
    close("Log");
    
// well5
// well5_white
for (i = 0; i < list_well5_white.length; i++) {
    showProgress(i + 1, list_well5_white.length);
    open(dir_well5_white + list_well5_white[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    run("Invert");
    // 縦
    makeLine(x1_well5, y1_well5, x2_well5, y2_well5);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well5_white + "result_well5_white" + i + ".csv");
    close("Log");


// well5_blue
for (i = 0; i < list_well5_blue.length; i++) {
    showProgress(i + 1, list_well5_blue.length);
    open(dir_well5_blue + list_well5_blue[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well5, y1_well5, x2_well5, y2_well5);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well5_blue + "result_well5_blue" + i + ".csv");
    close("Log");


// well5_green
for (i = 0; i < list_well5_green.length; i++) {
    showProgress(i + 1, list_well5_green.length);
    open(dir_well5_green + list_well5_green[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well5, y1_well5, x2_well5, y2_well5);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well5_green + "result_well5_green" + i + ".csv");
    close("Log");
    
// well6
// well6_white
for (i = 0; i < list_well6_white.length; i++) {
    showProgress(i + 1, list_well6_white.length);
    open(dir_well6_white + list_well6_white[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    run("Invert");
    // 縦
    makeLine(x1_well6, y1_well6, x2_well6, y2_well6);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well6_white + "result_well6_white" + i + ".csv");
    close("Log");


// well6_blue
for (i = 0; i < list_well6_blue.length; i++) {
    showProgress(i + 1, list_well6_blue.length);
    open(dir_well6_blue + list_well6_blue[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well6, y1_well6, x2_well6, y2_well6);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well6_blue + "result_well6_blue" + i + ".csv");
    close("Log");


// well6_green
for (i = 0; i < list_well6_green.length; i++) {
    showProgress(i + 1, list_well6_green.length);
    open(dir_well6_green + list_well6_green[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well6, y1_well6, x2_well6, y2_well6);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well6_green + "result_well6_green" + i + ".csv");
    close("Log");
    
// well7
// well7_white
for (i = 0; i < list_well7_white.length; i++) {
    showProgress(i + 1, list_well7_white.length);
    open(dir_well7_white + list_well7_white[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    run("Invert");
    // 縦
    makeLine(x1_well7, y1_well7, x2_well7, y2_well7);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well7_white + "result_well7_white" + i + ".csv");
    close("Log");


// well7_blue
for (i = 0; i < list_well7_blue.length; i++) {
    showProgress(i + 1, list_well7_blue.length);
    open(dir_well7_blue + list_well7_blue[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well7, y1_well7, x2_well7, y2_well7);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well7_blue + "result_well7_blue" + i + ".csv");
    close("Log");


// well7_green
for (i = 0; i < list_well7_green.length; i++) {
    showProgress(i + 1, list_well7_green.length);
    open(dir_well7_green + list_well7_green[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well7, y1_well7, x2_well7, y2_well7);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well7_green + "result_well7_green" + i + ".csv");
    close("Log");
    
// well8
// well8_white
for (i = 0; i < list_well8_white.length; i++) {
    showProgress(i + 1, list_well8_white.length);
    open(dir_well8_white + list_well8_white[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    run("Invert");
    // 縦
    makeLine(x1_well8, y1_well8, x2_well8, y2_well8);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well8_white + "result_well8_white" + i + ".csv");
    close("Log");


// well8_blue
for (i = 0; i < list_well8_blue.length; i++) {
    showProgress(i + 1, list_well8_blue.length);
    open(dir_well8_blue + list_well8_blue[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well8, y1_well8, x2_well8, y2_well8);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well8_blue + "result_well8_blue" + i + ".csv");
    close("Log");


// well8_green
for (i = 0; i < list_well8_green.length; i++) {
    showProgress(i + 1, list_well8_green.length);
    open(dir_well8_green + list_well8_green[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well8, y1_well8, x2_well8, y2_well8);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well8_green + "result_well8_green" + i + ".csv");
    close("Log");// 
    
//well9
// well9_white
for (i = 0; i < list_well9_white.length; i++) {
    showProgress(i + 1, list_well9_white.length);
    open(dir_well9_white + list_well9_white[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    run("Invert");
    // 縦
    makeLine(x1_well9, y1_well9, x2_well9, y2_well9);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well9_white + "result_well9_white" + i + ".csv");
    close("Log");


// well9_blue
for (i = 0; i < list_well9_blue.length; i++) {
    showProgress(i + 1, list_well9_blue.length);
    open(dir_well9_blue + list_well9_blue[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well9, y1_well9, x2_well9, y2_well9);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well9_blue + "result_well9_blue" + i + ".csv");
    close("Log");


// well9_green
for (i = 0; i < list_well9_green.length; i++) {
    showProgress(i + 1, list_well9_green.length);
    open(dir_well9_green + list_well9_green[i]);
    // INSERT MACRO HERE
    // please change oval
    run("8-bit");
    // 縦
    makeLine(x1_well9, y1_well9, x2_well9, y2_well9);
    pf = getProfile();
    Array.print(pf);
    close();
	}
    string = getInfo("Log");
    File.saveString(string, dir_well9_green + "result_well9_green" + i + ".csv");
    close("Log");
    










