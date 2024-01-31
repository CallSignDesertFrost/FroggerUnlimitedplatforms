import com.badlogic.gdx.Game;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.utils.Array;

public class FroggerGame extends Game {
    SpriteBatch batch;
    Texture frogTexture;
    Sprite frog;
    Array<Sprite> obstacles;
    float obstacleSpawnRate = 100;
    int score = 0;

    @Override
    public void create() {
        batch = new SpriteBatch();
        frogTexture = new Texture("frog.png");
        frog = new Sprite(frogTexture);
        frog.setPosition(Gdx.graphics.getWidth() / 2, Gdx.graphics.getHeight() - 100);

        obstacles = new Array<Sprite>();
        for (int i = 0; i < 5; i++) {
            spawnObstacle();
        }
    }

    @Override
    public void render() {
        super.render();

        // Handle user input
        if (Gdx.input.isKeyPressed(Input.Keys.UP))
            frog.setY(frog.getY() - 5);
        if (Gdx.input.isKeyPressed(Input.Keys.DOWN))
            frog.setY(frog.getY() + 5);
        if (Gdx.input.isKeyPressed(Input.Keys.LEFT))
            frog.setX(frog.getX() - 5);
        if (Gdx.input.isKeyPressed(Input.Keys.RIGHT))
            frog.setX(frog.getX() + 5);

        // Spawn obstacles
        if (MathUtils.random(0, obstacleSpawnRate) == 0) {
            spawnObstacle();
        }

        // Update the obstacles
        for (int i = 0; i < obstacles.size; i++) {
            Sprite obstacle = obstacles.get(i);
            obstacle.setX(obstacle.getX() - 3);

            // Remove obstacles that have moved off-screen
            if (obstacle.getX() < 0) {
                obstacles.removeIndex(i);
                i--;
            }