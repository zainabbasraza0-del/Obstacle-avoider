import tkinter as tk
import random
import time
import math
import json

class PerfectObstacleAvoider:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🚀 OBSTACLE AVOIDER DELUXE 🚀")
        self.root.geometry("800x800")
        self.root.resizable(False, False)
        
        # Main canvas
        self.canvas = tk.Canvas(
            self.root, 
            width=800, 
            height=800, 
            bg='#0a0f1a',
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Game variables
        self.player_size = 25
        self.player_x = 400
        self.player_y = 400
        self.player_speed = 10
        
        # Obstacles
        self.obstacles_x = []
        self.obstacles_y = []
        self.obstacles_speed = []
        self.obstacles_color = []
        self.obstacles_size = []
        
        # Difficulty settings
        self.difficulties = {
            'EASY': {'spawn': 0.02, 'speed': 2, 'size': 22, 'color': '#44ff44'},
            'NORMAL': {'spawn': 0.03, 'speed': 3, 'size': 20, 'color': '#ffff44'},
            'HARD': {'spawn': 0.04, 'speed': 4, 'size': 18, 'color': '#ff8844'},
            'INSANE': {'spawn': 0.05, 'speed': 5, 'size': 16, 'color': '#ff4444'}
        }
        self.current_diff = 'NORMAL'
        
        # Score tracking
        self.score = 0
        self.high_score = 0
        self.load_high_score()
        
        # Game state
        self.game_state = "LOADING"
        self.keys = {'Up': False, 'Down': False, 'Left': False, 'Right': False}
        self.game_over = False
        
        # Time tracking
        self.last_score_update = time.time()
        self.last_spawn_time = time.time()
        self.last_frame_time = time.time()
        self.fps = 60
        
        # Load high score
        self.load_high_score()
        
        # Setup keys
        self.setup_keys()
        
        # Start with loading screen
        self.show_loading_screen()
    
    def setup_keys(self):
        """Setup keyboard controls"""
        self.root.bind('<KeyPress>', self.key_down)
        self.root.bind('<KeyRelease>', self.key_up)
        self.root.bind('<r>', self.restart_game)
        self.root.bind('<R>', self.restart_game)
        self.root.bind('<Escape>', self.back_to_menu)
        self.root.focus_set()
    
    def key_down(self, event):
        if self.game_state == "PLAYING" and not self.game_over:
            if event.keysym in self.keys:
                self.keys[event.keysym] = True
    
    def key_up(self, event):
        if event.keysym in self.keys:
            self.keys[event.keysym] = False
    
    def restart_game(self, event=None):
        if self.game_state == "GAME_OVER":
            self.show_menu()
        else:
            self.start_game(self.current_diff)
    
    def back_to_menu(self, event=None):
        self.show_menu()
    
    def show_loading_screen(self):
        """Loading screen animation"""
        self.canvas.delete("all")
        self.game_state = "LOADING"
        
        # Background
        self.canvas.create_rectangle(0, 0, 800, 800, fill='#000000', outline='')
        
        # Title
        self.canvas.create_text(400, 250, text="OBSTACLE AVOIDER", 
                               fill='#44ff44', font=('Arial', 36, 'bold'))
        
        # Loading bar
        self.canvas.create_rectangle(200, 400, 600, 440, fill='#222222', outline='#44ff44', width=3)
        self.loading_bar = self.canvas.create_rectangle(202, 402, 202, 438, fill='#44ff44', outline='')
        
        # Loading text
        self.loading_text = self.canvas.create_text(400, 480, text="LOADING 0%", 
                                                    fill='white', font=('Arial', 16))
        
        # Tips
        self.tips = [
            "Use ARROW KEYS to move in all directions",
            "Avoid the colored obstacles!",
            "Higher score = faster obstacles",
            "Press R to restart anytime",
            "Press ESC for menu",
            "Different colors = different difficulties"
        ]
        self.tip_text = self.canvas.create_text(400, 550, text=random.choice(self.tips), 
                                                fill='#888888', font=('Arial', 14))
        
        # Animate
        self.load_progress = 0
        self.animate_loading()
    
    def animate_loading(self):
        """Loading animation"""
        self.load_progress += 1
        
        # Update bar
        bar_width = min(396, int(self.load_progress * 3.96))
        self.canvas.coords(self.loading_bar, 202, 402, 202 + bar_width, 438)
        
        # Update text
        percent = min(100, self.load_progress)
        self.canvas.itemconfig(self.loading_text, text=f"LOADING {percent}%")
        
        # Change tip every 20%
        if self.load_progress % 20 == 0:
            self.canvas.itemconfig(self.tip_text, text=random.choice(self.tips))
        
        if self.load_progress < 100:
            self.root.after(20, self.animate_loading)
        else:
            self.root.after(300, self.show_menu)
    
    def show_menu(self):
        """Main menu"""
        self.game_state = "MENU"
        self.canvas.delete("all")
        
        # Background
        self.canvas.create_rectangle(0, 0, 800, 800, fill='#0a0f1a', outline='')
        
        # Decorative grid
        for i in range(0, 801, 50):
            self.canvas.create_line(i, 0, i, 800, fill='#1a1f2a', width=1)
            self.canvas.create_line(0, i, 800, i, fill='#1a1f2a', width=1)
        
        # Title
        self.canvas.create_text(400, 120, text="🌟 OBSTACLE AVOIDER 🌟", 
                               fill='#44ff44', font=('Arial', 32, 'bold'))
        
        # Subtitle
        self.canvas.create_text(400, 170, text="4-WAY MOVEMENT", 
                               fill='#888888', font=('Arial', 16))
        
        # High score display
        self.canvas.create_text(400, 220, text=f"HIGH SCORE: {self.high_score}", 
                               fill='#ffff44', font=('Arial', 20, 'bold'))
        
        # Difficulty selection
        y_pos = 300
        for diff in self.difficulties:
            color = self.difficulties[diff]['color']
            
            # Button background
            btn = self.canvas.create_rectangle(250, y_pos-20, 550, y_pos+20,
                                              fill='#1a1f2a', outline=color, width=3)
            # Button text
            txt = self.canvas.create_text(400, y_pos, text=diff,
                                         fill=color, font=('Arial', 18, 'bold'))
            
            # Bind click
            for item in (btn, txt):
                self.canvas.tag_bind(item, '<Button-1>', lambda e, d=diff: self.start_game(d))
                self.canvas.tag_bind(item, '<Enter>', lambda e, c=color: self.hover_effect(e, c))
                self.canvas.tag_bind(item, '<Leave>', self.unhover_effect)
            
            y_pos += 50
        
        # Instructions
        self.canvas.create_text(400, 550, text="CONTROLS:", 
                               fill='white', font=('Arial', 14, 'bold'))
        self.canvas.create_text(400, 580, text="ARROW KEYS - Move in all directions", 
                               fill='#888888', font=('Arial', 12))
        self.canvas.create_text(400, 605, text="R - Restart | ESC - Menu", 
                               fill='#888888', font=('Arial', 12))
    
    def hover_effect(self, event, color):
        """Button hover effect"""
        self.canvas.itemconfig(event.widget.find_withtag("current"), fill=color, width=4)
    
    def unhover_effect(self, event):
        """Button unhover effect"""
        self.canvas.itemconfig(event.widget.find_withtag("current"), width=3)
    
    def start_game(self, difficulty):
        """Start new game"""
        self.game_state = "PLAYING"
        self.current_diff = difficulty
        settings = self.difficulties[difficulty]
        
        # Reset game state
        self.player_x = 400
        self.player_y = 400
        self.player_size = 25
        self.player_speed = 10
        self.score = 0
        self.game_over = False
        
        # Clear obstacles
        self.obstacles_x = []
        self.obstacles_y = []
        self.obstacles_speed = []
        self.obstacles_color = []
        self.obstacles_size = []
        
        # Set difficulty
        self.spawn_rate = settings['spawn']
        self.base_speed = settings['speed']
        self.obstacle_base_size = settings['size']
        
        # Reset keys
        for key in self.keys:
            self.keys[key] = False
        
        # Reset timers
        self.last_score_update = time.time()
        self.last_spawn_time = time.time()
        self.last_frame_time = time.time()
        
        # Start game loop
        self.game_loop()
    
    def game_loop(self):
        """Main game loop"""
        if self.game_state != "PLAYING" or self.game_over:
            return
        
        frame_start = time.time()
        
        # Update player
        self.update_player()
        
        # Update obstacles
        self.update_obstacles()
        
        # Spawn obstacles
        current_time = time.time()
        if current_time - self.last_spawn_time > 1/30:  # Limit spawn rate
            if random.random() < self.spawn_rate and len(self.obstacles_x) < 30:
                self.spawn_obstacle()
            self.last_spawn_time = current_time
        
        # Update score (every second)
        if current_time - self.last_score_update >= 1:
            self.score += 10
            self.last_score_update = current_time
        
        # Check collisions
        self.check_collisions()
        
        # Render
        self.render()
        
        # Calculate FPS
        frame_time = time.time() - frame_start
        target_time = 1/60  # Target 60 FPS
        sleep_time = max(0.001, target_time - frame_time)
        
        # Update FPS counter
        self.frame_times = getattr(self, 'frame_times', [])
        self.frame_times.append(frame_time)
        if len(self.frame_times) > 30:
            self.frame_times.pop(0)
        if self.frame_times:
            self.fps = int(1 / (sum(self.frame_times) / len(self.frame_times)))
        
        self.root.after(int(sleep_time * 1000), self.game_loop)
    
    def update_player(self):
        """4-way player movement"""
        dx, dy = 0, 0
        
        if self.keys['Up'] and self.player_y > self.player_size:
            dy = -self.player_speed
        if self.keys['Down'] and self.player_y < 800 - self.player_size:
            dy = self.player_speed
        if self.keys['Left'] and self.player_x > self.player_size:
            dx = -self.player_speed
        if self.keys['Right'] and self.player_x < 800 - self.player_size:
            dx = self.player_speed
        
        self.player_x += dx
        self.player_y += dy
    
    def spawn_obstacle(self):
        """Spawn new obstacle"""
        side = random.randint(0, 3)
        
        if side == 0:  # top
            x = random.randint(50, 750)
            y = -30
        elif side == 1:  # right
            x = 830
            y = random.randint(50, 750)
        elif side == 2:  # bottom
            x = random.randint(50, 750)
            y = 830
        else:  # left
            x = -30
            y = random.randint(50, 750)
        
        # Speed increases with score
        speed = self.base_speed + (self.score / 200)
        
        self.obstacles_x.append(x)
        self.obstacles_y.append(y)
        self.obstacles_speed.append(speed)
        self.obstacles_color.append(random.choice(['#ff4444', '#ff6b6b', '#ff8888', '#ffaa00']))
        self.obstacles_size.append(self.obstacle_base_size)
    
    def update_obstacles(self):
        """Move obstacles toward player"""
        for i in range(len(self.obstacles_x)):
            dx = self.player_x - self.obstacles_x[i]
            dy = self.player_y - self.obstacles_y[i]
            dist = math.hypot(dx, dy)
            
            if dist > 0:
                self.obstacles_x[i] += (dx / dist) * self.obstacles_speed[i]
                self.obstacles_y[i] += (dy / dist) * self.obstacles_speed[i]
        
        # Remove off-screen obstacles
        i = 0
        while i < len(self.obstacles_x):
            if (self.obstacles_x[i] < -100 or self.obstacles_x[i] > 900 or
                self.obstacles_y[i] < -100 or self.obstacles_y[i] > 900):
                self.obstacles_x.pop(i)
                self.obstacles_y.pop(i)
                self.obstacles_speed.pop(i)
                self.obstacles_color.pop(i)
                self.obstacles_size.pop(i)
            else:
                i += 1
    
    def check_collisions(self):
        """Check player-obstacle collisions"""
        px1 = self.player_x - self.player_size
        py1 = self.player_y - self.player_size
        px2 = self.player_x + self.player_size
        py2 = self.player_y + self.player_size
        
        for i in range(len(self.obstacles_x)):
            size = self.obstacles_size[i]
            ox1 = self.obstacles_x[i] - size
            oy1 = self.obstacles_y[i] - size
            ox2 = self.obstacles_x[i] + size
            oy2 = self.obstacles_y[i] + size
            
            if not (px2 < ox1 or px1 > ox2 or py2 < oy1 or py1 > oy2):
                self.game_over = True
                self.game_state = "GAME_OVER"
                
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.save_high_score()
                
                self.show_game_over()
                break
    
    def render(self):
        """Render everything"""
        self.canvas.delete('all')
        
        # Background grid
        for i in range(0, 801, 40):
            self.canvas.create_line(i, 0, i, 800, fill='#1a1f2a', width=1)
            self.canvas.create_line(0, i, 800, i, fill='#1a1f2a', width=1)
        
        # Draw obstacles
        for i in range(len(self.obstacles_x)):
            x = self.obstacles_x[i]
            y = self.obstacles_y[i]
            size = self.obstacles_size[i]
            color = self.obstacles_color[i]
            
            # Draw with glow
            for g in range(2, 0, -1):
                self.canvas.create_oval(
                    x - size - g, y - size - g,
                    x + size + g, y + size + g,
                    fill='', outline=color, width=g
                )
            
            # Main obstacle
            self.canvas.create_oval(
                x - size, y - size,
                x + size, y + size,
                fill=color, outline='white', width=1
            )
        
        # Draw player with glow
        for g in range(3, 0, -1):
            self.canvas.create_oval(
                self.player_x - self.player_size - g,
                self.player_y - self.player_size - g,
                self.player_x + self.player_size + g,
                self.player_y + self.player_size + g,
                fill='', outline='#44ffff', width=g
            )
        
        # Main player
        self.canvas.create_oval(
            self.player_x - self.player_size,
            self.player_y - self.player_size,
            self.player_x + self.player_size,
            self.player_y + self.player_size,
            fill='#44ffff', outline='white', width=2
        )
        
        # Player eyes
        eye_size = self.player_size // 4
        eye_offset = self.player_size // 3
        
        # Left eye
        self.canvas.create_oval(
            self.player_x - eye_offset - eye_size,
            self.player_y - eye_offset,
            self.player_x - eye_offset + eye_size,
            self.player_y - eye_offset + eye_size*2,
            fill='white'
        )
        self.canvas.create_oval(
            self.player_x - eye_offset - eye_size//2,
            self.player_y - eye_offset + eye_size//2,
            self.player_x - eye_offset,
            self.player_y - eye_offset + eye_size,
            fill='black'
        )
        
        # Right eye
        self.canvas.create_oval(
            self.player_x + eye_offset - eye_size,
            self.player_y - eye_offset,
            self.player_x + eye_offset + eye_size,
            self.player_y - eye_offset + eye_size*2,
            fill='white'
        )
        self.canvas.create_oval(
            self.player_x + eye_offset - eye_size//2,
            self.player_y - eye_offset + eye_size//2,
            self.player_x + eye_offset,
            self.player_y - eye_offset + eye_size,
            fill='black'
        )
        
        # UI
        diff_color = self.difficulties[self.current_diff]['color']
        
        # Score panel
        self.canvas.create_rectangle(20, 15, 180, 70, fill='#0a0f1a', outline=diff_color, width=2)
        self.canvas.create_text(40, 35, text="SCORE", fill='#888888', font=('Arial', 10), anchor='w')
        self.canvas.create_text(40, 55, text=str(self.score), fill='white', font=('Arial', 16, 'bold'), anchor='w')
        
        # High score
        self.canvas.create_text(160, 55, text=f"🏆 {self.high_score}", fill='#ffff44', font=('Arial', 12), anchor='e')
        
        # Difficulty
        self.canvas.create_text(760, 35, text=self.current_diff, fill=diff_color, font=('Arial', 14, 'bold'), anchor='e')
        
        # FPS
        self.canvas.create_text(760, 60, text=f"{self.fps}FPS", fill='#44ff44', font=('Arial', 10), anchor='e')
        
        # Obstacle count
        self.canvas.create_text(760, 80, text=f"OBJ: {len(self.obstacles_x)}", fill='#888888', font=('Arial', 10), anchor='e')
    
    def show_game_over(self):
        """Game over screen"""
        self.canvas.delete('all')
        
        # Dark overlay
        self.canvas.create_rectangle(0, 0, 800, 800, fill='black', stipple='gray25')
        
        # Game over text
        self.canvas.create_text(400, 300, text="GAME OVER", 
                               fill='#ff4444', font=('Arial', 48, 'bold'))
        
        # Score
        self.canvas.create_text(400, 380, text=f"SCORE: {self.score}", 
                               fill='white', font=('Arial', 24))
        
        # High score message
        if self.score == self.high_score and self.score > 0:
            self.canvas.create_text(400, 430, text="🎉 NEW HIGH SCORE! 🎉", 
                                   fill='#ffff44', font=('Arial', 18))
        
        # Difficulty
        diff_color = self.difficulties[self.current_diff]['color']
        self.canvas.create_text(400, 480, text=f"DIFFICULTY: {self.current_diff}", 
                               fill=diff_color, font=('Arial', 14))
        
        # Buttons
        # Menu button
        menu_btn = self.canvas.create_rectangle(250, 530, 370, 570,
                                               fill='#1a1f2a', outline='#44ff44', width=2)
        menu_txt = self.canvas.create_text(310, 550, text="MENU", 
                                          fill='#44ff44', font=('Arial', 12, 'bold'))
        
        # Restart button
        restart_btn = self.canvas.create_rectangle(430, 530, 550, 570,
                                                  fill='#1a1f2a', outline='#ffff44', width=2)
        restart_txt = self.canvas.create_text(490, 550, text="RESTART", 
                                             fill='#ffff44', font=('Arial', 12, 'bold'))
        
       # Bind buttons
        self.canvas.tag_bind(menu_btn, '<Button-1>', lambda e: self.show_menu())
        self.canvas.tag_bind(menu_txt, '<Button-1>', lambda e: self.show_menu())
        self.canvas.tag_bind(restart_btn, '<Button-1>', lambda e: self.start_game(self.current_diff))
        self.canvas.tag_bind(restart_txt, '<Button-1>', lambda e: self.start_game(self.current_diff))
        
        # Hint
        self.canvas.create_text(400, 630, text="Press R to restart | ESC for menu", 
                               fill='#888888', font=('Arial', 12))
    
    def load_high_score(self):
        """Load high score from file"""
        try:
            with open('highscore.json', 'r') as f:
                self.high_score = int(f.read())
        except:
            self.high_score = 0
    
    def save_high_score(self):
        """Save high score to file"""
        try:
            with open('highscore.json', 'w') as f:
                f.write(str(self.high_score))
        except:
            pass

# Run the game
if __name__ == "__main__":
    game = PerfectObstacleAvoider()
    game.root.mainloop()
    #saving the loop to a variable to prevent garbage collection issues
    
         
       
         