package main

import (
	"image/color"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/theme"
)

type MinimalDarkTheme struct{}

func (MinimalDarkTheme) Color(name fyne.ThemeColorName, variant fyne.ThemeVariant) color.Color {
	switch name {
	case theme.ColorNameBackground:
		return color.RGBA{R: 30, G: 30, B: 30, A: 255}
	case theme.ColorNameButton:
		return color.RGBA{R: 45, G: 45, B: 45, A: 255}
	case theme.ColorNameDisabled:
		return color.RGBA{R: 80, G: 80, B: 80, A: 255}
	case theme.ColorNameDisabledButton:
		return color.RGBA{R: 55, G: 55, B: 55, A: 255}
	case theme.ColorNameFocus:
		return color.RGBA{R: 100, G: 150, B: 255, A: 255}
	case theme.ColorNameForeground:
		return color.White
	case theme.ColorNameHover:
		return color.RGBA{R: 60, G: 60, B: 60, A: 255}
	case theme.ColorNameInputBackground:
		return color.RGBA{R: 40, G: 40, B: 40, A: 255}
	case theme.ColorNamePlaceHolder:
		return color.RGBA{R: 130, G: 130, B: 130, A: 255}
	case theme.ColorNamePressed:
		return color.RGBA{R: 75, G: 75, B: 75, A: 255}
	default:
		return theme.DefaultTheme().Color(name, variant)
	}
}

func (MinimalDarkTheme) Font(style fyne.TextStyle) fyne.Resource {
	return theme.DefaultTheme().Font(style)
}

func (MinimalDarkTheme) Icon(name fyne.ThemeIconName) fyne.Resource {
	return theme.DefaultTheme().Icon(name)
}

func (MinimalDarkTheme) Size(name fyne.ThemeSizeName) float32 {
	switch name {
	case theme.SizeNamePadding:
		return 0
	case theme.SizeNameText:
		return 14
	case theme.SizeNameInputBorder:
		return 2
	default:
		return theme.DefaultTheme().Size(name)
	}
}
