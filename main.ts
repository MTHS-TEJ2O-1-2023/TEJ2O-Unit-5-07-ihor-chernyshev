/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Ihor Chernyshev
 * Created on: Nov 2023
 * This program controls a servo.
*/

// variables
const servoNumber1 = robotbit.Servos.S1

// setup
basic.showIcon(IconNames.Happy)

// button A
input.onButtonPressed(Button.A, function () {
  // goes to 0 degrees
  robotbit.Servo(servoNumber1, 0)
  basic.clearScreen()
  basic.showNumber(0)
  basic.showIcon(IconNames.SmallSquare)
  basic.clearScreen()
  basic.showIcon(IconNames.Happy)
})

// button B
input.onButtonPressed(Button.B, function () {
  // goes to 180 degrees
  robotbit.Servo(servoNumber1, 180)
  basic.clearScreen()
  basic.showNumber(180)
  basic.showIcon(IconNames.SmallSquare)
  basic.clearScreen()
  basic.showIcon(IconNames.Happy)
})
