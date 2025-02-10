// Package weather provide details about the weather in Goblinocus.
package weather

// CurrentCondition contains the details about the weather current condition.
var CurrentCondition string

// CurrentLocation contains the details about the current location.
var CurrentLocation string

// Forecast returns a string joining the current location and the current condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
