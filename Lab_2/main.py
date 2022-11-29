if __name__ == '__main__':
    # main video settings
    VIDEO_DPI = 1000
    VIDEO_FPS = 60
    VIDEO_WIDTH = 1080
    VIDEO_HEIGHT = 720

    # the proportion of keyboard display
    KB_RATIO = 0.1

    # speed of the falling tiles (pixels per sec)
    TILE_VELOCITY = 500

    import piano_tile_Creator

    ptc = piano_tile_Creator.PianoTileCreator(video_width=VIDEO_WIDTH,
                                              video_height=VIDEO_HEIGHT,
                                              video_dpi=VIDEO_DPI,
                                              video_fps=VIDEO_FPS,
                                              KB_ratio=KB_RATIO,
                                              tile_velocity=TILE_VELOCITY,
                                              key_color="purple",
                                              showKeyVelocity=True)

    ptc.load_midi_file("files/believer.mid", verbose=True)
    ptc.render("files/believer.mp4", verbose=True)
