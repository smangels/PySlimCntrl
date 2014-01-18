from time import sleep
import libbcm2835._bcm2835 as soc

BCM2835_GPIO_FSEL_INPT = 0
BCM2835_GPIO_FSEL_OUTP = 1
BCM2835_GPIO_FSEL_ALT0 = 2

BCM2835_GPIO_PUD_OFF = 0
BCM2835_GPIO_PUD_DOWN = 1
BCM2835_GPIO_PUD_UP = 2

BCM2835_SPI_MSBFIRST = 1
BCM2835_SPI_LSBFIRST = 0

BCM2835_SPI_MODE0 = 0	# CPOL = 0, CPHA = 0
BCM2835_SPI_MODE1 = 1   # CPOL = 0, CPHA = 1
BCM2835_SPI_MODE2 = 2   # CPOL = 1, CPHA = 0
BCM2835_SPI_MODE3 = 3   # CPOL = 1, CPHA = 1

BCM2835_SPI_CLK_500k = 512
BCM2835_SPI_CLK_125k = 2048
BCM2835_SPI_CLK_250k = 1024
BCM2835_SPI_CLK_62k5 = 4096
BCM2835_SPI_CLK_31k2 = 8192
BCM2835_SPI_CLK_15k6 = 16384
BCM2835_SPI_CLK_8k0 = 32768
BCM2835_SPI_CLK_4k0 = 0

BCM2835_SPI_CS0 = 0
BCM2835_SPI_CS1 = 1
BCM2835_SPI_CS2 = 2
BCM2835_SPI_CSM = 3	# manual CS

PIN_BTN_01 = 27
PIN_BTN_02 = 22
PIN_BTN_03 = 23
PIN_BTN_04 = 24
PIN_BTN_05 = 4
PIN_BTN_06 = 17

PIN_LCD_RST = 25
PIN_LCD_CS = 8
PIN_LCD_RS = 7
PIN_LCD_MOSI = 10
PIN_LCD_SCLK = 11
PIN_LCD_BACKLIGHT = 18

class Lcd_Emsystech(object):

	"""
	Controls the graphical LCD provided by Emsystech
	Runs 64x128 pixel, background light using GPIOs
	Controllable contrast
	"""

	def __init__(self):
		"""
		Contructor
		"""
		self.debug = False
		self.logger = None
		self.spi = None
		self.initialised = False
		self.contrast = 0
		self.__socInit()
		self.__spiInit()
		self.__lcdInit()
		self.contrastSet(5)
		self.backlight_on()
		self.fb = array('B')
	

	def __del__(self):
		self.backlight_off()
		if self.spi:
			soc.bcm2835_spi_end()
			print('SPI disabled')

		self.__socReset()
		print('BCM down')

	def __spiInit(self):
		soc.bcm2835_spi_begin()
		soc.bcm2835_spi_setBitOrder(BCM2835_SPI_MSBFIRST)
		soc.bcm2835_spi_setDataMode(BCM2835_SPI_MODE3)
		soc.bcm2835_spi_setClockDivider(BCM2835_SPI_CLK_500k)
		soc.bcm2835_spi_chipSelect(BCM2835_SPI_CS0)
		soc.bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, 0)
		#soc.bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS1, 0)
		soc.bcm2835_gpio_fsel(PIN_LCD_RS, BCM2835_GPIO_FSEL_OUTP)
		soc.bcm2835_gpio_set(PIN_LCD_RS)
		self.spi = True

		print('lcd.__spiInit')
		return True


	def backlight_on(self):
		if not self.initialised:
			return False
		soc.bcm2835_gpio_set(PIN_LCD_BACKLIGHT)
		print('Backlight Enabled')
		return True

	def backlight_off(self):
		if not self.initialised:
			return False
		print('Backlight Disabled')
		soc.bcm2835_gpio_clr(PIN_LCD_BACKLIGHT)
		return True

	def contrastSet(self, contrast):
		if not self.initialised:
			return False
		if contrast < 0 or contrast > 9:
			print('invalid contrast=', contrast)
			return False
		print('LCD.contrast: old= ', self.contrast, ' new=', contrast)
		self.__lcdWriteCmd(0x81)
		self.__lcdWriteCmd(contrast)
		self.contrast = contrast

	def lcdDrawLine(self, x0, y0, len):
		print('lcd.drawLine: x0=', x0, ' y0=', y0, ' len=', len)
		return True

	def lcdPutPixel(self, x, y, color):
		print('lcd.putPixel: x=', x, ' y=', y, ' color=', color)
		return True

	def lcdPrintTxt(self, x, y, txt):
		print('lcd.print: x=', x, ' y=', y, ' txt=', txt)
		return True

	def __socInit(self):
		print('BCM.__socInit')
		if not soc.bcm2835_init():
			print('soc.init failed')
			return False

		soc.bcm2835_gpio_fsel(17, BCM2835_GPIO_FSEL_INPT)
		soc.bcm2835_gpio_fsel(27, BCM2835_GPIO_FSEL_INPT)
		soc.bcm2835_gpio_fsel(22, BCM2835_GPIO_FSEL_INPT)
		soc.bcm2835_gpio_fsel(23, BCM2835_GPIO_FSEL_INPT)
		soc.bcm2835_gpio_fsel(24, BCM2835_GPIO_FSEL_INPT)

		soc.bcm2835_gpio_set_pud(17, BCM2835_GPIO_PUD_UP)
		soc.bcm2835_gpio_set_pud(27, BCM2835_GPIO_PUD_UP)
		soc.bcm2835_gpio_set_pud(22, BCM2835_GPIO_PUD_UP)
		soc.bcm2835_gpio_set_pud(23, BCM2835_GPIO_PUD_UP)
		soc.bcm2835_gpio_set_pud(24, BCM2835_GPIO_PUD_UP)

		soc.bcm2835_gpio_fsel(PIN_LCD_BACKLIGHT, BCM2835_GPIO_FSEL_OUTP)	
		#soc.bcm2835_gpio_fsel(PIN_LCD_RS, BCM2835_GPIO_FSEL_OUTP)
		soc.bcm2835_gpio_fsel(PIN_LCD_RST, BCM2835_GPIO_FSEL_OUTP)
		#soc.bcm2835_gpio_fsel(PIN_LCD_CS, BCM2835_GPIO_FSEL_OUTP)	
		#soc.bcm2835_gpio_set(PIN_LCD_CS)		
		soc.bcm2835_gpio_set(PIN_LCD_RST)
	
		self.initialised = True
		print('LCD.__socInit finished')
		return True

	def __socReset(self):
		soc.bcm2835_gpio_set_pud(17, BCM2835_GPIO_PUD_OFF)
		soc.bcm2835_gpio_set_pud(27, BCM2835_GPIO_PUD_OFF)
		soc.bcm2835_gpio_set_pud(22, BCM2835_GPIO_PUD_OFF)
		soc.bcm2835_gpio_set_pud(23, BCM2835_GPIO_PUD_OFF)
		soc.bcm2835_gpio_set_pud(24, BCM2835_GPIO_PUD_OFF)
		soc.bcm2835_close()
		self.initialised = False
		print('LCD.__socReset')


	def __lcdInit(self):
		if not self.initialised:
			return False
		soc.bcm2835_gpio_clr(PIN_LCD_RST)
		soc.bcm2835_delay(50)
		soc.bcm2835_gpio_set(PIN_LCD_RST)
		soc.bcm2835_delay(200)
		self.__lcdWriteCmd(0xE2)
		self.__lcdWriteCmd(0x40)
		self.__lcdWriteCmd(0xA1)
		self.__lcdWriteCmd(0xC0)
		self.__lcdWriteCmd(0xA4)
		self.__lcdWriteCmd(0xA6)
		self.__lcdWriteCmd(0xA2)
		self.__lcdWriteCmd(0x2F)
		self.__lcdWriteCmd(0x27)

		self.__lcdWriteCmd(0x81)
		self.__lcdWriteCmd(0x08)

		self.__lcdWriteCmd(0xFA)
		self.__lcdWriteCmd(0x90)
		self.__lcdWriteCmd(0xAF)

		print('LCD.__lcdInit')
		return True


	def __lcdWriteCmd(self, command):
		if not self.initialised:
			return False
		if command < 0 and command > 255:
			print('invalid data: ', command)
			return False
		print('LCD.__lcdWriteCMD: ', command)
		soc.bcm2835_gpio_clr(PIN_LCD_RS)
		soc.bcm2835_spi_transfer(command & 0xFF)
		soc.bcm2835_gpio_set(PIN_LCD_RS)
		return True
	
	def __lcdWriteData(self, data):
		if not self.initialised:
			return False
		print('LCD.__lcdWriteFB', data)
		soc.bcm2835_gpio_set(PIN_LCD_RS)
		soc.bcm2835_spi_transfer(data & 0xFF)
		return True

	def __lcdSetXY(self, x, y):
		if not self.initialised:
			return False
		print('LCD.__lcdSetXY, x=', x, ' page=', y)
		x = x + 4
		self.__lcdWriteCmd(0x00 + (x & 0x0F))
		self.__lcdWriteCmd(0x10 + ((x >> 4) & 0x0F))
		self.__lcdWriteCmd(0xB0 + (y & 0x07))
		return True
		

