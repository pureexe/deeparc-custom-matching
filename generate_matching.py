import argparse

def main(args):
    arc_begin = arc_end = ring_begin = ring_end  = args.window_size // 2
    if args.window_size % 2 == 0:
        arc_begin -= 1
        ring_begin -= 1
    with open(args.output,'w') as f:
        for pivot_arc in range(args.arc_size):
            for pivot_ring in range(args.ring_size):
                start_arc = pivot_arc - arc_begin
                stop_arc = pivot_arc + arc_end + 1
                start_ring = pivot_ring - ring_begin
                stop_ring = pivot_ring + ring_end + 1
                list_arc = list(filter(lambda x: (x >= 0 and x < args.arc_size),range(start_arc,stop_arc)))
                list_ring = list(map(lambda x: x % args.ring_size,range(start_ring,stop_ring)))
                for current_arc in list_arc:
                    for current_ring in list_ring:
                        if current_arc <= pivot_arc and current_ring <= pivot_ring:
                            continue 
                        pivot_name = args.name.format(arc=pivot_arc,ring=pivot_ring)
                        current_name = args.name.format(arc=current_arc,ring=current_ring)
                        f.write('{} {}\n'.format(pivot_name,current_name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='generate_matching.py - list the file name for colmap!'
    )
    parser.add_argument(
        '--name',
        type=str,
        default='cam{arc:03d}/cam{arc:03d}_{ring:05d}.jpg',
        help='format of image relative path',
    )
    parser.add_argument(
        '-w',
        '--window-size',
        type=int,
        default=5,
        help='size of window to consider to the image NxN (default:5)'
    )
    parser.add_argument(
        '-a',
        '--arc-size',
        type=int,
        default=10,
        help='number of camera in arc (default:10)'
    )
    parser.add_argument(
        '-r',
        '--ring-size',
        type=int,
        default=41,
        help='number of servo step (default:41)'
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default='output/matching.txt',

    )
    main(parser.parse_args())
