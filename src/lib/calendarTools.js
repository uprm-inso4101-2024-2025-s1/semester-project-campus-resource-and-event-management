// takes in a month number (1 to 12) and returns the number of days in the month
export function getDaysInMonth(month, year) {
  return new Date(year, month, 0).getDate();
}

// takes in a month number (1 to 12) and returns the number of days in the month
export function getMonthName(month) {
  return [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ][(month - 1) % 12]; // wrapping around months to prevent errors
}

export function getDayOfTheWeek(day, month, year) {
  return [
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
  ][new Date(year, month-1, day).getDay()]
}