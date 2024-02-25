import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.meta.api.methods.send.SendMessage;
import org.telegram.telegrambots.meta.api.objects.Update;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;

public class MeetingRoomBot extends TelegramLongPollingBot {
    private final String BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"; // Замените на ваш токен бота
    private final String BOT_USERNAME = "your_bot_username"; // Замените на имя вашего бота

    @Override
    public void onUpdateReceived(Update update) {
        if (update.hasMessage() && update.getMessage().hasText()) {
            String messageText = update.getMessage().getText();
            long chatId = update.getMessage().getChatId();

            if ("/start".equals(messageText)) {
                sendMessage(chatId, "Привет! Я помогу вам забронировать переговорную комнату.");
            } else if ("/book".equals(messageText)) {
                // Здесь должна быть логика резервирования комнаты
                sendMessage(chatId, "Вы успешно забронировали переговорную комнату на завтра в 10:00.");
            }
        }
    }

    private void sendMessage(long chatId, String messageText) {
        SendMessage message = new SendMessage();
        message.setChatId(chatId);
        message.setText(messageText);
        try {
            execute(message);
        } catch (TelegramApiException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String getBotUsername() {
        return BOT_USERNAME;
    }

    @Override
    public String getBotToken() {
        return BOT_TOKEN;
    }
}