import subprocess


cassandra_host = '172.27.89.125'
cassandra_port = 9042
keyspace = 'cs2_keyspace_5'
tables = [ 'cs2_fen_structure', 'cs2_game_termination', 'cs2_games', 'cs2_move_eval', 'cs2_movestack', 'cs2_player_stats', 'cs2_players' ]

output_dir = 'output'

def export_table_to_csv(keyspace, table, output_dir):
    # Construct the COPY command
    copy_command = f"cqlsh {cassandra_host} {cassandra_port} -e \"COPY {keyspace}.{table} TO '{output_dir}/{table}.csv' WITH HEADER = true;\""
    print(copy_command)

    # Execute the COPY command
    subprocess.run(copy_command, shell=True, check=True)

# Main function
def main():

    for table in tables:
        export_table_to_csv(keyspace, table, output_dir)
        print(f"Exporting {table} to CSV...")

if __name__ == "__main__":
    main()
