import net.dv8tion.jda.api.AccountType;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

import javax.security.auth.login.LoginException;
public class Main extends ListenerAdapter {
public static void main(String[] args) throws LoginException {
    String token="Nzk2MzI4NTM5NDY0Nzk0MTIz.X_WUvg.WtHCp5SwcqtXFp9Z_RX8WKe1Qas";
    JDABuilder builder=JDABuilder.createDefault(token);
    builder.addEventListeners(new Main());
    builder.build();


}

    @Override
    public void onMessageReceived(@NotNull MessageReceivedEvent event) {
        System.out.println("meassage recived"+event.getAuthor().getName()+":"+event.getMessage().getContentDisplay());
        if(event.getMessage().getContentRaw().equals("!ping"))
        {
            event.getChannel().sendMessage("Pong").queue();
        }
}
}

