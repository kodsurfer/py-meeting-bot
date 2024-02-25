package main

import (
	"log"
	"time"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
)

const (
	token = "YOUR_TELEGRAM_BOT_TOKEN" // Замените на ваш токен бота
)

func main() {
	bot, err := tgbotapi.NewBotAPI(token)
	if err != nil {
		log.Panic(err)
	}

	bot.Debug = true

	log.Printf("Authorized on account %s", bot.Self.UserName)

	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates := bot.GetUpdatesChan(u)

	for update := range updates {
		if update.Message == nil { // Проверяем, что сообщение не пустое
			continue
		}

		log.Printf("[%s] %s", update.Message.From.UserName, update.Message.Text)

		// Обрабатываем команду /start
		if update.Message.Text == "/start" {
			msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Привет! Я помогу вам забронировать переговорную комнату.")
			bot.Send(msg)
		}

		// Обрабатываем команду /book
		if update.Message.Text == "/book" {
			// Здесь должна быть логика резервирования комнаты
			msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Вы успешно забронировали переговорную комнату на завтра в 10:00.")
			bot.Send(msg)
		}
	}
}