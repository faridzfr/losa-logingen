```markdown
# Lost Saga Login Command Generator

Generates login command for private/self-hosted Lost Saga using Python and cryptography.
```
## FIX_EXPIRED_KEY Procedure
In most cases, the error message `"UserNodeManager::OnResultSelectUserLoginInfo : Error Expire Key:"` in logs means that `conndate` does not match the local time. It's recommended to change `GETDATE()` in the `Fix_Expired_Key` procedure to the local timezone for more accurate `conndate`

```sql
ALTER PROCEDURE [dbo].[FIX_EXPIRED_KEY]
(
    @userNum INT
)
AS
BEGIN
    UPDATE userLoginDB
    SET connDate = GETDATE() AT TIME ZONE 'UTC' AT TIME ZONE 'SE Asia Standard Time'
    WHERE accountIDX = @userNum;
END
```

Timezone mappings: [Timezone Mappings](https://gist.github.com/alejzeis/ad5827eb14b5c22109ba652a1a267af5)

## Features

- Generates a command to execute a game launcher.
- Saves the output command to a `.bat` file for easy execution.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/faridzfr/losa-logingen.git
   cd losa-logingen
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script and input data:

```bash
python logingen.py
```

### Example Data

- **App name without extension** (default: `lostsaga`)
- **Local version** (default: `119483910`)
- **Game server ID** (default: `82558251637056`)
- **User encode** (default: `111111111111111`)
- **User ID** (default: `devk`)
- **Agent encode** (default: `Y9h3Z3u1c0gQF55`)
- **Real IP** (default: `0.0.0.0`)
- **Local IPv4** (default: `127.0.0.1`)

### Example Output

```bash
start lostsaga.exe EDEW3940FVDP4950,10,20,30,1,autoupgrade_info.ini,-1,0,1,119483910,?eae0ca332fb475f9f9d8daf598471c9d4391d0?0?d2a2dda62b1136c814d0959a5610917c?82558251637056?2010,7,15,1?10201?
```

### Output File

Script creates `lostart.bat` file. Move it to client folder, run FIX_EXPIRED_KEY procedure and run `lostart.bat`.

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to this project.

## License

This project is licensed under the MIT License.

### `requirements.txt`

```bash
cryptography
```
