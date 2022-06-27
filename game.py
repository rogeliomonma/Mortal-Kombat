#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys
from pygame.locals import *
from pygame.sprite import Sprite
#Iniciación de Pygame
pygame.init()
#Música de fondo
icono=pygame.image.load('icon.png')
pygame.mixer.music.load('sonido/mortal-kombat-round-one.ogg')
pygame.mixer.music.play(-1)
class Personaje(Sprite):
	def __init__(self):
		self.image = personaje = pygame.image.load("Imagenes/goku.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(50, 300)
		self.muerto = 0
	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_e]:
			self.image = personaje = pygame.image.load("Imagenes/subatact.gif").convert_alpha()
		elif kamehameha.rect.x > 860:
			self.image = personaje = pygame.image.load("Imagenes/subringh.gif").convert_alpha()

		if teclas[K_LEFT]:
			self.image = personaje = pygame.image.load("Imagenes/subleft.gif").convert_alpha()
			if self.rect.x > 0:
				self.rect.x -= 10
		elif teclas[K_RIGHT]:
			self.image = personaje = pygame.image.load("Imagenes/sunrigh.gif").convert_alpha()
			if self.rect.x < 740:
				self.rect.x += 10

		if teclas[K_UP]:
			self.image = personaje = pygame.image.load("Imagenes/subup.gif").convert_alpha()
			if self.rect.y > 32:
				self.rect.y -= 10
		elif teclas[K_DOWN]:
			if self.rect.y < 530:
				self.image = personaje = pygame.image.load("Imagenes/sundown.gif").convert_alpha()
				self.rect.y += 10

class Kamehameha(Sprite):
	def __init__(self):
		self.image = kamehameha = pygame.image.load("Imagenes/subbol.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(900, 700)
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.rect.x > 840:
			if teclas[K_e]:
				self.rect.x = (personaje.rect.x + 60)
				self.rect.y = (personaje.rect.y + 14)
		if self.rect.x < 870:
			self.rect.x += 20

class Barravidagoku(Sprite):
	def __init__(self):
		self.image = barravidagoku = pygame.image.load("Imagenes/barravidagoku.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(18, 4)
	def update(self):
		if barravidagoku.rect.x <= -152:
			personaje.muerto = 1
		if disparo.rect.y >= (personaje.rect.y - 56):
			if disparo.rect.y <= (personaje.rect.y + 62):
				if disparo.rect.x >= personaje.rect.x:
					if disparo.rect.x <= (personaje.rect.x + 43):
						barravidagoku.rect.x -= 26
						disparo.rect.x = -400
		if minicell.rect.y >= (personaje.rect.y - 56):
			if minicell.rect.y <= (personaje.rect.y + 62):
				if minicell.rect.x >= personaje.rect.x:
					if minicell.rect.x <= (personaje.rect.x + 43):
						barravidagoku.rect.x -= 26
						disparo.rect.x = -400

class Minicell(Sprite):
	def __init__(self):
		self.image = minicell = pygame.image.load("Imagenes/scorp.gif").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(750, 300)
		self.bandera = 0
		self.muerto = 0
	def update(self):
		if self.rect.y == 40:
			self.bandera = 0
		elif self.rect.y == 540:
			self.bandera = 1

		if self.bandera == 0:
			self.rect.y += 10
		elif self.bandera == 1:
			self.rect.y -= 10
	def dificil(self):
		if self.rect.x < 0:
			self.rect.x = 800
		if self.rect.y > 600:
			self.rect.y = 0
		self.rect.x -= 10
		self.rect.y += 10

class Disparo(Sprite):
	def __init__(self):
		self.image = barravidagoku = pygame.image.load("Imagenes/boolfuego.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(-400, -400)
	def update(self):
		if self.rect.x == -400:
			if minicell.rect.y == personaje.rect.y:
				self.rect.x = (minicell.rect.x - 60)
				self.rect.y = (minicell.rect.y - 14)
		if self.rect.x > -400:
			self.rect.x -= 5

class Barravidaminicell(Sprite):
	def __init__(self):
		self.image = barravidaminicell = pygame.image.load("Imagenes/barravidaminicell.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(712, 4)
	def update(self):
		if self.rect.x >= 882:
			minicell.muerto = 1
		if kamehameha.rect.y >= minicell.rect.y:
			if kamehameha.rect.y <= (minicell.rect.y + 62):
				if kamehameha.rect.x >= minicell.rect.x:
					if kamehameha.rect.x <= (minicell.rect.x + 43):
						self.rect.x += 6
						kamehameha.rect.x = 900

if __name__ == '__main__':
	# Variables.
	salir = False
	

	# Establezco la pantalla.
	screen = pygame.display.set_mode((900,600))

	# Establezco el título.
	pygame.display.set_caption("MORTAL KOMBAT")

	# Creo dos objetos surface.
	fondo = pygame.image.load("Imagenes/mortal.png").convert()
	cuadrovidagoku = pygame.image.load("Imagenes/cuadrovidagoku.png").convert_alpha()
	cuadrovidaminicell = pygame.image.load("Imagenes/cuadrovidaminicell.png").convert_alpha()
	hasperdido = pygame.image.load("Imagenes/Hasperdido.png").convert()
	hasganado = pygame.image.load("Imagenes/Hasganado.png").convert()
	# .convert() convierten la superficie a un formato de color que permite imprimirlas mucho mas rápido.

	# Objetos
	temporizador = pygame.time.Clock()
	personaje = Personaje()

	kamehameha = Kamehameha()
	minicell = Minicell()
	disparo = Disparo()
	barravidagoku = Barravidagoku()
	barravidaminicell = Barravidaminicell()
	xx=0
	if xx<1:
		pygame.time.delay(2000)
		pygame.mixer.music.load('sonido/mortal-kombat-2.ogg')
		pygame.mixer.music.play(-1)
		xx=2


	# Movimiento del personaje.
	while not salir:
	
		personaje.update()
		kamehameha.update()
		if barravidaminicell.rect.x < 797:
			minicell.update()
		else:
			minicell.dificil()
		disparo.update()
		barravidagoku.update()
		barravidaminicell.update()

		# actualizacion grafica
		screen.blit(fondo, (0, 0))
		screen.blit(personaje.image, personaje.rect)
	
		screen.blit(kamehameha.image, kamehameha.rect)
		screen.blit(minicell.image, minicell.rect)
		screen.blit(disparo.image, disparo.rect)
		screen.blit(barravidagoku.image, barravidagoku.rect)
		screen.blit(barravidaminicell.image, barravidaminicell.rect)
		screen.blit(cuadrovidagoku, (0,0))
		screen.blit(cuadrovidaminicell, (709,0))
		if personaje.muerto == 1:
			screen.blit(hasperdido, (250,264))
			pygame.mixer.music.load('sonido/mortal-kombat-finish-her.ogg')
			pygame.mixer.music.play(-1)
		if minicell.muerto == 1:
			screen.blit(hasganado, (250,264))
		pygame.display.flip()

		if personaje.muerto == 1:
			pygame.time.delay(2000)
			salir = True
		elif minicell.muerto == 1:
			pygame.time.delay(3000)
			salir = True
		temporizador.tick(60)

		# gestion de eventos
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				salir = True
