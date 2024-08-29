# https://ffmpeg.org/ffmpeg.html
# https://python-ffmpeg.readthedocs.io/en/stable/
# https://download.blender.org/peach/bigbuckbunny_movies/
import argparse

from ffmpeg_benchmark import probe
from ffmpeg_benchmark import transcode
from ffmpeg_benchmark import psnr
# from ffmpeg_benchmark import vmaf
from ffmpeg_benchmark.loggers import logger

ACTIONS = {
    'probe': probe.main,
    'transcode': transcode.main,
    'psnr': psnr.main,
    # 'vmaf': vmaf.main,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", type=int, default=0, help="0: Muted, 1: Info, 2: Verbose")
    parser.add_argument(
        '-q', '--quiet',
        action="store_true",
        help="Completly disable any output",
    )

    subparsers = parser.add_subparsers(dest="action")
    probe.make_parser(subparsers)
    transcode.make_parser(subparsers)
    psnr.make_parser(subparsers)
    # vvmaf.make_parser(subparsers)

    args = parser.parse_args()

    verbosity = args.verbosity
    if args.quiet:
        verbosity = 0
        logger.setLevel(40-(10+verbosity*10))

    action = ACTIONS[args.action]
    result = action(args)

    result.update(
    )
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    main()