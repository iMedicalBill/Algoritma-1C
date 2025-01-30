import turtle
import random
from tkinter import messagebox
import pygame
import time
import sys
import traceback

class Game:
    def _init_(self):
        try:
            self.level = 1
            self.score = 0
            self.state = "playing"
            self.lives = 3
            self.frame_rate = 1/60
            
            # Initialize sound
            print("Initializing pygame mixer...")
            pygame.mixer.init()
            self.load_sounds()
            
            # Initialize screen
            print("Setting up screen...")
            self.screen = turtle.Screen()
            self.setup_screen()
            
            # Initialize pen for drawing
            self.pen = turtle.Turtle()
            self.pen.hideturtle()
            
            self.running = True
            print("Game initialization complete")
            
        except Exception as e:
            print(f"Error in Game initialization: {e}")
            print(traceback.format_exc())
            raise
            
    def load_sounds(self):
        self.sounds = {}
        sound_files = {
            'explosion': 'explosion.mp3',
            'laser': 'laser.mp3',
            'hyperspace': 'hyperspace.mp3'
        }
        
        print("Loading sound files...")
        for name, file in sound_files.items():
            try:
                self.sounds[name] = pygame.mixer.Sound(file)
                print(f"Loaded {file}")
            except Exception as e:
                print(f"Warning: Could not load {file}: {e}")
                
    def setup_screen(self):
        self.screen.bgcolor("black")
        try:
            self.screen.bgpic("starfield.gif")
        except Exception as e:
            print(f"Warning: Could not load background image: {e}")
        self.screen.tracer(0)
        
    def play_sound(self, sound_name):
        try:
            if sound_name in self.sounds:
                self.sounds[sound_name].play()
        except Exception as e:
            print(f"Warning: Could not play sound {sound_name}: {e}")
            
    def draw_border(self):
        try:
            self.pen.clear()
            self.pen.penup()
            self.pen.goto(-300, 300)
            self.pen.pendown()
            self.pen.color("white")
            self.pen.pensize(3)
            for _ in range(4):
                self.pen.forward(600)
                self.pen.right(90)
        except Exception as e:
            print(f"Error drawing border: {e}")
            
    def show_status(self):
        try:
            self.pen.penup()
            self.pen.goto(-290, 310)
            self.pen.color("white")
            if self.lives > 0:
                msg = f"Level: {self.level} Lives: {self.lives} Score: {self.score}"
            else:
                msg = f"Game Over Score: {self.score}"
            self.pen.clear()
            self.pen.write(msg, font=("Arial", 16, "normal"))
        except Exception as e:
            print(f"Error showing status: {e}")
        
    def cleanup(self):
        try:
            pygame.mixer.quit()
            if self.running:
                self.running = False
                self.screen.bye()
        except Exception as e:
            print(f"Error during cleanup: {e}")

class Sprite(turtle.Turtle):
    def _init_(self, shape, color, x, y):
        try:
            super()._init_(shape=shape)
            self.penup()
            self.speed(0)
            self.color(color)
            self.goto(x, y)
            self.velocity = 0
        except Exception as e:
            print(f"Error creating sprite: {e}")
            raise
        
    def is_collision(self, other):
        try:
            return self.distance(other) < 20
        except Exception as e:
            print(f"Error checking collision: {e}")
            return False
        
    def move(self):
        try:
            self.forward(self.velocity)
            
            # Boundary checking
            x = max(-290, min(290, self.xcor()))
            y = max(-290, min(290, self.ycor()))
            
            if x != self.xcor() or y != self.ycor():
                self.goto(x, y)
                self.right(random.randint(20, 60))
        except Exception as e:
            print(f"Error moving sprite: {e}")

class Player(Sprite):
    def _init_(self, x, y):
        try:
            super()._init_("triangle", "white", x, y)
            self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
            self.velocity = 0
        except Exception as e:
            print(f"Error creating player: {e}")
            raise
        
    def turn_left(self):
        try:
            self.left(30)
        except Exception as e:
            print(f"Error turning left: {e}")
        
    def turn_right(self):
        try:
            self.right(30)
        except Exception as e:
            print(f"Error turning right: {e}")
        
    def accelerate(self):
        try:
            self.velocity += 1
            if self.velocity > 10:
                self.velocity = 10
        except Exception as e:
            print(f"Error accelerating: {e}")
        
    def decelerate(self):
        try:
            self.velocity = max(0, self.velocity - 0.5)
        except Exception as e:
            print(f"Error decelerating: {e}")

class Enemy(Sprite):
    def __init__(self, x, y):
        try:
            super().__init__("circle", "red", x, y)
            self.velocity = 4
            self.setheading(random.randint(0, 360))
        except Exception as e:
            print(f"Error creating enemy: {e}")
            raise

class Ally(Sprite):
    def __init__(self, x, y):
        try:
            super()._init_("square", "blue", x, y)
            self.velocity = 6
            self.setheading(random.randint(0, 360))
        except Exception as e:
            print(f"Error creating ally: {e}")
            raise
        
    def avoid(self, other):
        try:
            if self.distance(other) < 40:
                self.left(30)
        except Exception as e:
            print(f"Error in avoid behavior: {e}")

class Bullet(Sprite):
    def __init__(self):
        try:
            super()._init_("triangle", "yellow", -1000, 1000)
            self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
            self.hideturtle()
            self.velocity = 20
            self.status = "ready"
        except Exception as e:
            print(f"Error creating bullet: {e}")
            raise
        
    def fire(self, player, game):
        try:
            if self.status == "ready":
                game.play_sound('laser')
                self.goto(player.xcor(), player.ycor())
                self.setheading(player.heading())
                self.showturtle()
                self.status = "firing"
        except Exception as e:
            print(f"Error firing bullet: {e}")
            
    def move(self):
        try:
            if self.status == "firing":
                self.forward(self.velocity)
                
                if abs(self.xcor()) > 290 or abs(self.ycor()) > 290:
                    self.status = "ready"
                    self.hideturtle()
                    self.goto(-1000, 1000)
        except Exception as e:
            print(f"Error moving bullet: {e}")

class Particle(Sprite):
    def __init__(self, color):
        try:
            super()._init_("circle", color, -1000, -1000)
            self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
            self.frame = 0
        except Exception as e:
            print(f"Error creating particle: {e}")
            raise
        
    def explode(self, x, y):
        try:
            self.goto(x, y)
            self.setheading(random.randint(0, 360))
            self.frame = 1
        except Exception as e:
            print(f"Error in particle explosion: {e}")
        
    def move(self):
        try:
            if self.frame > 0:
                self.forward(18 - self.frame)
                self.frame += 1
                
                if self.frame < 6:
                    self.shapesize(0.3, 0.3)
                elif self.frame < 11:
                    self.shapesize(0.2, 0.2)
                else:
                    self.shapesize(0.1, 0.1)
                    
                if self.frame > 18:
                    self.frame = 0
                    self.goto(-1000, -1000)
        except Exception as e:
            print(f"Error moving particle: {e}")

def setup_game():
    try:
        print("Starting game setup...")
        game = Game()
        player = Player(0, 0)
        bullet = Bullet()
        
        # Create enemies
        enemies = [Enemy(random.randint(-200, 200), random.randint(-200, 200)) 
                  for _ in range(6)]
        
        # Create allies
        allies = [Ally(random.randint(-200, 200), random.randint(-200, 200)) 
                 for _ in range(6)]
        
        # Create particles
        particles = []
        for color in ['yellow', 'red', 'orange']:
            particles.extend([Particle(color) for _ in range(2)])
        
        # Set up keyboard bindings
        game.screen.onkey(player.turn_left, "Left")
        game.screen.onkey(player.turn_right, "Right")
        game.screen.onkey(player.accelerate, "Up")
        game.screen.onkey(player.decelerate, "Down")
        game.screen.onkey(lambda: bullet.fire(player, game), "space")
        game.screen.listen()
        
        print("Game setup complete")
        return game, player, bullet, enemies, allies, particles
    except Exception as e:
        print(f"Error in game setup: {e}")
        print(traceback.format_exc())
        raise

def main():
    try:
        print("Starting game...")
        game, player, bullet, enemies, allies, particles = setup_game()
        
        game.draw_border()
        game.show_status()
        
        print("Entering main game loop...")
        while game.running:
            try:
                current_time = time.time()
                
                if game.state == "playing":
                    player.move()
                    bullet.move()
                    
                    for enemy in enemies:
                        enemy.move()
                        
                        if player.is_collision(enemy):
                            game.play_sound('explosion')
                            player.color("red")
                            for particle in particles:
                                particle.explode(enemy.xcor(), enemy.ycor())
                            enemy.goto(random.randint(-200, 200), random.randint(-200, 200))
                            game.lives -= 1
                            game.show_status()
                            player.color("white")
                            
                            if game.lives < 1:
                                game.state = "gameover"
                        
                        if bullet.status == "firing" and bullet.is_collision(enemy):
                            game.play_sound('explosion')
                            for particle in particles:
                                particle.explode(enemy.xcor(), enemy.ycor())
                            bullet.status = "ready"
                            bullet.hideturtle()
                            enemy.goto(random.randint(-200, 200), random.randint(-200, 200))
                            game.score += 100
                            game.show_status()
                    
                    for ally in allies:
                        ally.move()
                        for enemy in enemies:
                            ally.avoid(enemy)
                        ally.avoid(player)
                        
                        if bullet.status == "firing" and bullet.is_collision(ally):
                            game.play_sound('explosion')
                            for particle in particles:
                                particle.explode(ally.xcor(), ally.ycor())
                            bullet.status = "ready"
                            bullet.hideturtle()
                            ally.goto(random.randint(-200, 200), random.randint(-200, 200))
                            game.score -= 50
                            game.show_status()
                    
                    for particle in particles:
                        particle.move()
                        
                elif game.state == "gameover":
                    for _ in range(360):
                        player.right(1)
                        if game.running:
                            game.screen.update()
                    
                    if messagebox.askyesno("Game Over", "Play again?"):
                        game.lives = 3
                        game.score = 0
                        game.state = "playing"
                        player.velocity = 0
                        player.goto(0, 0)
                        player.setheading(0)
                        
                        for enemy in enemies:
                            enemy.goto(random.randint(-200, 200), random.randint(-200, 200))
                        for ally in allies:
                            ally.goto(random.randint(-200, 200), random.randint(-200, 200))
                    else:
                        game.running = False
                        break
                
                if game.running:
                    game.screen.update()
                    elapsed = time.time() - current_time
                    if elapsed < game.frame_rate:
                        time.sleep(game.frame_rate - elapsed)
                    
            except Exception as e:
                print(f"Error in game loop: {e}")
                print(traceback.format_exc())
                break
                
    except Exception as e:
        print(f"Critical error: {e}")
        print(traceback.format_exc())
    finally:
        print("Cleaning up...")
        try:
            game.cleanup()
        except Exception as e:
            print(f"Error during cleanup: {e}")

if __name__ == "__main__":
    main()