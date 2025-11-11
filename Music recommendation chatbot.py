import tkinter as tk
import nltk
from nltk.corpus import wordnet as wn
import json
import os
import webbrowser
import re

nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# --- Song database 
songs = {
    "happy": [
        {"title": "Happy", "artist": "Pharrell Williams", "album": "Girl"},
        {"title": "Uptown Funk", "artist": "Bruno Mars", "album": "Uptown Special"},
        {"title": "Walking on Sunshine", "artist": "Katrina and the Waves", "album": "Katrina and the Waves"},
        {"title": "Can't Stop the Feeling!", "artist": "Justin Timberlake", "album": "Trolls"},
        {"title": "Shake It Off", "artist": "Taylor Swift", "album": "1989"},
        {"title": "Best Day of My Life", "artist": "American Authors", "album": "Oh, What a Life"},
        {"title": "I'm Still Standing", "artist": "Elton John", "album": "Jump Up!"},
        {"title": "Good as Hell", "artist": "Lizzo", "album": "Coconut Oil"},
        {"title": "Morni Banke", "artist": "Guru Randhawa", "album": "Badshah"},
        {"title": "Tareefan", "artist": "Badshah", "album": "Veere Di Wedding"},
        {"title": "Badtameez Dil", "artist": "Benny Dayal", "album": "Yeh Jawaani Hai Deewani"},
        {"title": "London Thumakda", "artist": "Neha Kakkar / Sonu Kakkar", "album": "Queen"},
        {"title": "Kala Chashma", "artist": "Badshah / Amar Arshi", "album": "Baar Baar Dekho"},
        {"title": "Kar Gayi Chull", "artist": "Badshah", "album": "Kapoor & Sons"},
        {"title": "Bom Diggy", "artist": "Zack Knight & Jasmin Walia", "album": "Single"}
    ],
    "sad": [
        {"title": "Someone Like You", "artist": "Adele", "album": "21"},
        {"title": "Fix You", "artist": "Coldplay", "album": "X&Y"},
        {"title": "Tears Dry on Their Own", "artist": "Amy Winehouse", "album": "The Other Side of Amy Winehouse"},
        {"title": "The Sound of Silence", "artist": "Simon & Garfunkel", "album": "Parsley, Sage, Rosemary and Thyme"},
        {"title": "Hurt", "artist": "Johnny Cash", "album": "American IV: The Man Comes Around"},
        {"title": "Yesterday", "artist": "The Beatles", "album": "Help!"},
        {"title": "Skinny Love", "artist": "Bon Iver", "album": "For Emma, Forever Ago"},
        {"title": "Channa Mereya", "artist": "Arijit Singh", "album": "Ae Dil Hai Mushkil"},
        {"title": "Dil Dhadakne Do", "artist": "Priyanka Chopra", "album": "Zindagi Na Milegi Dobara"},
        {"title": "Tujhe Kitna Chahne Lage", "artist": "Arijit Singh", "album": "Kabir Singh"},
        {"title": "Agar Tum Saath Ho", "artist": "Alka Yagnik / Arijit Singh", "album": "Tamasha"},
        {"title": "Kabira (Encore)", "artist": "Arijit Singh", "album": "Yeh Jawaani Hai Deewani"},
        {"title": "Mere Sohneya", "artist": "Amit Mishra", "album": "Kabir Singh"},
        {"title": "Phir Le Aya Dil", "artist": "Rekha Bhardwaj", "album": "Barfi!"}
    ],
    "energetic": [
        {"title": "Eye of the Tiger", "artist": "Survivor", "album": "Eye of the Tiger"},
        {"title": "Stronger", "artist": "Kanye West", "album": "Graduation"},
        {"title": "We Will Rock You", "artist": "Queen", "album": "News of the World"},
        {"title": "Don't Stop Believin'", "artist": "Journey", "album": "Escape"},
        {"title": "Bang Bang", "artist": "Jessie J, Ariana Grande, Nicki Minaj", "album": "Sweet Talker"},
        {"title": "Thunder", "artist": "Imagine Dragons", "album": "Evolve"},
        {"title": "Run the World (Girls)", "artist": "Beyoncé", "album": "4"},
        {"title": "Feel This Moment", "artist": "Pitbull ft. Christina Aguilera", "album": "Global Warming"},
        {"title": "High Rated Gabru", "artist": "Guru Randhawa", "album": "Ishq Tera"},
        {"title": "Laung Laachi", "artist": "Mehndi Hasan", "album": "Laung Laachi"},
        {"title": "Malhari", "artist": "Vishal Dadlani", "album": "Bajirao Mastani"},
        {"title": "Jai Ho", "artist": "A. R. Rahman", "album": "Slumdog Millionaire"},
        {"title": "Sher Aaya Sher", "artist": "Divine", "album": "Single"},
        {"title": "Apna Time Aayega", "artist": "Rapsody / Divine", "album": "Gully Boy"},
        {"title": "Aila Re Aillaa", "artist": "Shankar Mahadevan", "album": "Simmba"}
    ],
    "relax": [
        {"title": "Weightless", "artist": "Marconi Union", "album": "Weightless"},
        {"title": "Chill Out", "artist": "John Legend", "album": "Evolver"},
        {"title": "Breezin'", "artist": "George Benson", "album": "Breezin'"},
        {"title": "Sunset Lover", "artist": "Petit Biscuit", "album": "Petit Biscuit"},
        {"title": "Watermark", "artist": "Enya", "album": "Watermark"},
        {"title": "River Flows in You", "artist": "Yiruma", "album": "First Love"},
        {"title": "Riverside", "artist": "Iggy Azalea", "album": "Savior"},
        {"title": "Ocean Eyes", "artist": "Billie Eilish", "album": "Don’t Smile at Me"},
        {"title": "Ik Vaari Aa", "artist": "Arijit Singh", "album": "Raabta"},
        {"title": "Sardar Udham", "artist": "B Praak", "album": "Sardar Udham"},
        {"title": "Kun Faya Kun", "artist": "A. R. Rahman", "album": "Rockstar"},
        {"title": "Kasoor", "artist": "Prateek Kuhad", "album": "Single"},
        {"title": "Phir Le Aya Dil (Reprise)", "artist": "Arijit Singh", "album": "Barfi!"},
        {"title": "Tu Hi Hai", "artist": "Mohit Chauhan", "album": "Dear Zindagi"}
    ],
    "romantic": [
        {"title": "Perfect", "artist": "Ed Sheeran", "album": "÷"},
        {"title": "All of Me", "artist": "John Legend", "album": "Love in the Future"},
        {"title": "Your Song", "artist": "Elton John", "album": "Elton John"},
        {"title": "A Thousand Years", "artist": "Christina Perri", "album": "The Twilight Saga: Breaking Dawn – Part 1"},
        {"title": "Make You Feel My Love", "artist": "Adele", "album": "19"},
        {"title": "Can't Help Falling in Love", "artist": "Elvis Presley", "album": "Blue Hawaii"},
        {"title": "Unchained Melody", "artist": "The Righteous Brothers", "album": "Just Once in My Life"},
        {"title": "Come Away With Me", "artist": "Norah Jones", "album": "Come Away With Me"},
        {"title": "Pehla Pyaar", "artist": "Arijit Singh", "album": "Kabir Singh"},
        {"title": "Jaanu", "artist": "Jaani", "album": "Jaanu"},
        {"title": "Tum Hi Ho", "artist": "Arijit Singh", "album": "Aashiqui 2"},
        {"title": "Raabta", "artist": "Arijit Singh", "album": "Agent Vinod"},
        {"title": "Tera Ban Jaunga", "artist": "Akhil Sachdeva", "album": "Kabir Singh"},
        {"title": "Bolna", "artist": "Arijit Singh", "album": "Kapoor & Sons"}
    ],
    "party": [
        {"title": "Party Rock Anthem", "artist": "LMFAO", "album": "Sorry for Party Rocking"},
        {"title": "I Gotta Feeling", "artist": "The Black Eyed Peas", "album": "The E.N.D."},
        {"title": "Tik Tok", "artist": "Kesha", "album": "Animal"},
        {"title": "Uptown Funk", "artist": "Bruno Mars", "album": "Uptown Special"},
        {"title": "Dance Monkey", "artist": "Tones and I", "album": "The Kids Are Coming"},
        {"title": "Despacito", "artist": "Luis Fonsi ft. Daddy Yankee", "album": "VIDA"},
        {"title": "Can’t Stop the Feeling!", "artist": "Justin Timberlake", "album": "Trolls"},
        {"title": "Hips Don't Lie", "artist": "Shakira ft. Wyclef Jean", "album": "Oral Fixation, Vol. 2"},
        {"title": "Genda Phool", "artist": "Badshah", "album": "Genda Phool"},
        {"title": "Sauda Khara Khara", "artist": "Diljit Dosanjh", "album": "Good Newwz"},
        {"title": "London Thumakda", "artist": "Various", "album": "Queen"},
        {"title": "Kala Chashma", "artist": "Amar Arshi / Badshah", "album": "Baar Baar Dekho"},
        {"title": "The Jawaani Song", "artist": "Vishal Dadlani", "album": "Jawaani Jaaneman"},
        {"title": "Angreji Beat", "artist": "Gippy Grewal / Yo Yo Honey Singh", "album": "Diljit Dosanjh - Single"}
    ],
    "inspirational": [
        {"title": "Rise Up", "artist": "Andra Day", "album": "Cheers to the Fall"},
        {"title": "Hall of Fame", "artist": "The Script ft. will.i.am", "album": "#3"},
        {"title": "Fight Song", "artist": "Rachel Platten", "album": "Wildfire"},
        {"title": "The Climb", "artist": "Miley Cyrus", "album": "Hannah Montana: The Movie"},
        {"title": "Don't Stop Believin'", "artist": "Journey", "album": "Escape"},
        {"title": "Stronger (What Doesn't Kill You)", "artist": "Kelly Clarkson", "album": "Stronger"},
        {"title": "Skyscraper", "artist": "Demi Lovato", "album": "Unbroken"},
        {"title": "Beautiful", "artist": "Christina Aguilera", "album": "Stripped"},
        {"title": "Dil Dhadakne Do", "artist": "Priyanka Chopra", "album": "Zindagi Na Milegi Dobara"},
        {"title": "Ik Onkar", "artist": "Harvinder Bittu", "album": "Sardar Udham Singh"},
        {"title": "Zinda", "artist": "Bhaiyyu", "album": "Bhaag Milkha Bhaag"},
        {"title": "Chak De India", "artist": "Sukhwinder Singh", "album": "Chak De India"},
        {"title": "Lakshya", "artist": "Shankar Mahadevan", "album": "Lakshya"}
    ]
}

# recommend_song function 
def recommend_song(user_input):
    tokens = nltk.word_tokenize(user_input.lower())
    mood_scores = {mood: 0 for mood in songs}

    for token in tokens:
        for mood in mood_scores:
            if token == mood:
                mood_scores[mood] += 2
            for syn in wn.synsets(token):
                for lemma in syn.lemmas():
                    if lemma.name().lower() == mood:
                        mood_scores[mood] += 1

    if all(score == 0 for score in mood_scores.values()):
        return "Sorry, I couldn't understand your mood. Can you specify if you're feeling happy, sad, energetic, or want to relax?"

    recommended_mood = max(mood_scores, key=mood_scores.get)
    recommendations = songs.get(recommended_mood, [])

    response_lines = []
    for song in recommendations:
        song_title = song.get("title", "")
        song_artist = song.get("artist", "")
        song_album = song.get("album", "")
        query = f"{song_title} {song_artist}"
        query_encoded = re.sub(r'\s+', '+', query.strip())
        youtube_search = f"https://www.youtube.com/results?search_query={query_encoded}"
        response_lines.append(f"{song_title} by {song_artist} (Album: {song_album})\n{youtube_search}")

    return "\n\n".join(response_lines)


#  Chatbot UI class with mood buttons and chat highlighting
class SongRecommenderChatbot:
    URL_REGEX = re.compile(r'(https?://[^\s]+)')

    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot Song Recommender")
        self.history = load_history()

        # fullscreen styling kept
        self.root.configure(bg="#837f7f")
        self.font_main = ('Segoe UI', 14)
        self.button_font = ('Segoe UI', 13, 'bold')

        # Chat area
        self.chat_area = tk.Text(root, wrap=tk.WORD, state='disabled', width=80, height=25,
                                 bg='#ffffff', fg='#000000', borderwidth=2, relief='sunken', font=self.font_main)
        self.chat_area.grid(column=0, row=0, columnspan=3, padx=20, pady=(16,8), sticky='nsew')
        self.append_message("Bot: Hello! I'm here to recommend you some great songs. Click a mood below or type how you feel.\n")

        # Configure grid to expand
        for c in range(3):
            self.root.grid_columnconfigure(c, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

      
        moods = ['happy', 'sad', 'energetic', 'relax', 'romantic', 'party', 'inspirational']
        self.mood_frame = tk.Frame(root, bg=self.root['bg'])
        self.mood_frame.grid(column=0, row=1, columnspan=3, padx=20, pady=(4,12), sticky='ew')

        self.mood_buttons = {}
        for i, mood in enumerate(moods):
            btn = tk.Button(self.mood_frame, text=mood.capitalize(), command=lambda m=mood: self.mood_clicked(m),
                            bg='#283843', fg='#ffffff', font=('Segoe UI', 11), relief='raised', padx=10, pady=6)
            btn.grid(row=0, column=i, padx=6, sticky='ew')
            self.mood_frame.grid_columnconfigure(i, weight=1)
            self.mood_buttons[mood] = btn

        # track currently selected mood
        self.selected_mood = None
        # highlight colors for buttons
        self.highlight_bg = '#1e88e5' 
        self.highlight_fg = '#ffffff'
        self.default_bg = '#283843'
        self.default_fg = '#ffffff'

        # Chat highlight colors per mood (subtle)
        self.chat_mood_colors = {
            'happy': {'bg': "#2c1c02", 'fg': '#000000'},
            'sad': {'bg': "#252728", 'fg': '#000000'},
            'energetic': {'bg': "#717270", 'fg': '#000000'},
            'relax': {'bg': '#f3e5f5', 'fg': '#000000'},
            'romantic': {'bg': "#d7627d", 'fg': '#000000'},
            'party': {'bg': "#b59731", 'fg': '#000000'},
            'inspirational': {'bg': "#235f28", 'fg': '#000000'}
        }

        # create tags in Text widget for each mood for consistent styling
        for mood, colors in self.chat_mood_colors.items():
            tag_name = f"mood_chat_{mood}"
            self.chat_area.tag_configure(tag_name, background=colors['bg'], foreground=colors['fg'], font=('Segoe UI', 14, 'bold'))

        # User input
        self.user_input = tk.Entry(root, width=60, bg='#e9eef0', fg='#000000', borderwidth=2, relief='groove',
                                   font=self.font_main)
        self.user_input.grid(column=0, row=2, padx=20, pady=8, columnspan=2, sticky='ew')
        self.user_input.bind("<Return>", self.process_input)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.process_input, bg='#338a3e', fg='#ffffff',
                                     font=self.button_font, relief='raised', padx=12, pady=6)
        self.send_button.grid(column=2, row=2, padx=20, pady=8, sticky='ew')

    def highlight_mood(self, mood):
        """Visually highlight the chosen mood button and un-highlight others."""
        for m, btn in self.mood_buttons.items():
            if m == mood:
                btn.configure(bg=self.highlight_bg, fg=self.highlight_fg, font=('Segoe UI', 11, 'bold'), relief='sunken')
            else:
                btn.configure(bg=self.default_bg, fg=self.default_fg, font=('Segoe UI', 11), relief='raised')
        self.selected_mood = mood

    def clear_mood_highlight(self):
        self.highlight_mood(None)

    def mood_clicked(self, mood):
        """Simulate the user typing the mood, highlight it, show recommendations, and highlight the chat line."""
        # highlight selected mood button
        self.highlight_mood(mood)
        # append user mood message and tag it in chat
        self.append_user_mood(mood)
        # Get recommendation and append bot response
        response = recommend_song(mood)
        self.append_message(f"Bot: {response}\n")

    def append_user_mood(self, mood):
        """Insert 'You: mood' into chat and tag that line with mood-specific chat tag."""
        self.chat_area.config(state='normal')
        start_index = self.chat_area.index(tk.END)  # insertion index
        self.chat_area.insert(tk.END, f"You: {mood}\n")
        end_index = self.chat_area.index(tk.END)
        tag_name = f"mood_chat_{mood}"
        # add tag across the inserted range
        self.chat_area.tag_add(tag_name, start_index, end_index)
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)
        # update links (no change)
        self.make_links_clickable()

    def tag_last_user_message(self, mood):
        """Find the last line that starts with 'You:' and tag it."""
        try:
            idx = self.chat_area.search(r"You:", "1.0", stopindex=tk.END, regexp=True, backwards=True)
        except tk.TclError:
            idx = None
            for i in range(1, 200):
                try_idx = f"end-{i}l"
                line = self.chat_area.get(try_idx + " linestart", try_idx + " lineend")
                if line.startswith("You:"):
                    idx = try_idx + " linestart"
                    break
        if idx:
            line_start = idx
            line_end = f"{line_start} lineend +1c"
            tag_name = f"mood_chat_{mood}"
            for m in self.chat_mood_colors:
                self.chat_area.tag_remove(f"mood_chat_{m}", line_start, line_end)
            self.chat_area.tag_add(tag_name, line_start, line_end)
            self.chat_area.yview(tk.END)

    def append_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message)
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)
        self.make_links_clickable()

    def make_links_clickable(self):
        content = self.chat_area.get("1.0", tk.END)
        # remove prior link tags to avoid duplicates
        for tag in list(self.chat_area.tag_names()):
            if tag.startswith("link_"):
                self.chat_area.tag_delete(tag)

        for i, match in enumerate(self.URL_REGEX.finditer(content)):
            url = match.group(0)
            start_index = f"1.0+{match.start()}c"
            end_index = f"1.0+{match.end()}c"
            tag_name = f"link_{i}"
            self.chat_area.tag_add(tag_name, start_index, end_index)
            self.chat_area.tag_config(tag_name, foreground="blue", underline=True)
            # bind to open specific url
            self.chat_area.tag_bind(tag_name, "<Button-1>", lambda e, url=url: webbrowser.open(url))

    def process_input(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text:
            return

        # display user message
        self.append_message(f"You: {user_text}\n")
        self.user_input.delete(0, tk.END)

        normalized = user_text.lower()
        # If user typed a direct mood that matches a mood button, highlight button and tag last user message
        if normalized in self.mood_buttons:
            self.highlight_mood(normalized)
            # tag the last 'You:' message in chat with the mood style
            self.tag_last_user_message(normalized)
        else:
            # no exact mood typed -> clear button highlights and remove mood tags from last user line (if any)
            self.clear_mood_highlight()

        if normalized in ['hi', 'hello', 'hey']:
            self.append_message("Bot: Hello! Click a mood below or type how you feel (e.g., happy, sad, energetic, relax, romantic, party, inspirational).\n")
        elif normalized == "show me a song":
            self.append_message("Bot: Please tell me how you're feeling (happy, sad, energetic, relax, romantic, party, inspirational).\n")
        elif normalized == "clear":
            # keep clear via typing 'clear'
            self.clear_chat()
        else:
            response = recommend_song(user_text)
            self.append_message(f"Bot: {response}\n")

    def clear_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state='disabled')

# --- Simple history helpers (unchanged) ---
def load_history():
    if os.path.exists('chat_history.json'):
        try:
            with open('chat_history.json', 'r') as file:
                return json.load(file)
        except Exception:
            return []
    return []

def save_history(history):
    with open('chat_history.json', 'w') as file:
        json.dump(history, file)


# --- Main: open fullscreen and run ---
def main():
    root = tk.Tk()
    # Open fullscreen
    try:
        root.attributes('-fullscreen', True)
    except Exception:
        try:
            root.state('zoomed')
        except Exception:
            pass

    # allow Esc to exit fullscreen
    def exit_fullscreen(event=None):
        try:
            root.attributes('-fullscreen', False)
        except Exception:
            try:
                root.state('normal')
            except Exception:
                pass
    root.bind("<Escape>", exit_fullscreen)

    bot = SongRecommenderChatbot(root)
    root.mainloop()

if __name__ == "__main__":
    main()
