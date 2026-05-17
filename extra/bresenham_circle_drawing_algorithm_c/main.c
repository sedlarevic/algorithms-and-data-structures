#include <stdio.h>
#include <SDL2/SDL.h>

void drawCircle(int xc, int yc, int x, int y, SDL_Renderer* renderer)
{
  SDL_RenderDrawPoint(renderer,xc+x,yc+y);
  SDL_RenderDrawPoint(renderer,xc-x,yc+y);
  SDL_RenderDrawPoint(renderer,xc+x,yc-y);
  SDL_RenderDrawPoint(renderer,xc-x,yc-y);
  SDL_RenderDrawPoint(renderer,xc+y,yc+x);
  SDL_RenderDrawPoint(renderer,xc-y,yc+x);
  SDL_RenderDrawPoint(renderer,xc+y,yc-x);
  SDL_RenderDrawPoint(renderer,xc-y,yc-x);
}

void bresenhamCircle(int xc, int yc, int r, SDL_Renderer* renderer)
{
  int p = 3 - 2 * r;
  int x = 0;
  int y = r;

  drawCircle(xc, yc, x, y,renderer);


  while(x<=y)
  {
    if (p < 0)
    {
      p = p + 4 * x + 6;
    }else
    {
      p = p + 4 * (x - y) + 10;
      y--;
    }
    x++;
    SDL_Delay(50);
    drawCircle(xc, yc, x, y, renderer);

  }

}

int main(int argc, char *argv[])
{


  SDL_Window* window = NULL;
  SDL_Renderer* renderer = NULL;
  if (SDL_Init(SDL_INIT_VIDEO) != 0) {
    printf("SDL_Init error: %s\n", SDL_GetError());
    return 1;
  }

  if (SDL_CreateWindowAndRenderer(640, 480, 0, &window, &renderer) != 0) {
    printf("CreateWindowAndRenderer error: %s\n", SDL_GetError());
    return 1;
  }
  SDL_SetRenderDrawColor(renderer,0,0,0,255);
  SDL_RenderClear(renderer);
  SDL_SetRenderDrawColor(renderer,255,255,255,255);
  SDL_RenderDrawPoint(renderer,640/2,480/2);
  int xc = 320;
  int yc = 240;
  int r = 50;
  bresenhamCircle(xc,yc,r,renderer);
  SDL_RenderPresent(renderer);

  SDL_Event e;
  int running = 1;

  while (running) {
      while (SDL_PollEvent(&e)) {
        if (e.type == SDL_QUIT)
            running = 0;
      }
  }

  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();

  return 0;
}
