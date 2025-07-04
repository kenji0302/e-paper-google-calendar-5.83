<?php
require("secret.php");
?>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }

    h1 {
      font-size: 24px;
      margin-bottom: 20px;
    }

    h2 {
      font-size: 20px;
      margin-top: 30px;
    }

    h3 {
      font-size: 18px;
    }

    input[type="text"] {
      width: 100%;
      max-width: 400px;
      padding: 8px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    input[type="submit"] {
      background-color: #4CAF50;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      margin: 10px 0;
    }

    input[type="submit"]:hover {
      background-color: #45a049;
    }

    a {
      display: inline-block;
      background-color: #008CBA;
      color: white;
      padding: 10px 20px;
      text-decoration: none;
      border-radius: 4px;
    }

    a:hover {
      background-color: #007399;
    }

    @media screen and (max-width: 480px) {
      body {
        padding: 10px;
      }

      h1 {
        font-size: 20px;
      }

      h2 {
        font-size: 18px;
      }

      h3 {
        font-size: 16px;
      }

      input[type="submit"] {
        width: 100%;
      }

      a {
        display: block;
        text-align: center;
      }
    }
  </style>
  <script>
    window.addEventListener('DOMContentLoaded', function() {
      const form = document.getElementById('myForm');
      const responseBox = document.getElementById('responseBox');

      form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const formData = new FormData(form);

        try {
          const response = await fetch('https://www.googleapis.com/oauth2/v4/token', {
            method: 'POST',
            body: formData
          });
          if (!response.ok) throw new Error('通信に失敗しました');

          const result = await response.json();

          if (result.refresh_token) {
            responseBox.value = result.refresh_token;
          } else {
            responseBox.value = 'refresh_tokenが見つかりません';
          }
        } catch (err) {
          responseBox.value = 'エラー';
          console.error(err);
        }
      });
    });
  </script>
</head>

<body>
  <h1>for e-paper 5.83 </h1>
  <h2>1. Google認証</h2>
  <p>
    <a href="https://accounts.google.com/o/oauth2/v2/auth?client_id=<?php echo $CLIENT_ID ?>&redirect_uri=<?php echo $REDIRECT_URI ?>&scope=https://www.googleapis.com/auth/calendar.readonly&response_type=code&access_type=offline&prompt=consent">認証</a>
  </p>
  <?php if (!empty($_GET['code'])) { ?>
    <h2>2. REFRESH TOKENの取得</h2>
    <p>
    <form method="post" id="myForm">
      <input type="hidden" name="code" value="<?php echo htmlentities($_GET['code']) ?>" />
      <input type="hidden" name="redirect_uri" value="<?php echo htmlentities($REDIRECT_URI) ?>" />
      <input type="hidden" name="client_id" value="<?php echo htmlentities($CLIENT_ID) ?>" />
      <input type="hidden" name="client_secret" value="<?php echo htmlentities($CLIENT_SECRET) ?>" />
      <input type="hidden" name="scope" value="" />
      <input type="hidden" name="grant_type" value="authorization_code" />
      <input type="hidden" name="prompt" value="true" />
      <input type="hidden" name="access_type" value="offline" />
      <input type="submit" value="取得" />
    </form>
    </p>
    <h3>REFRESH TOKEN</h3>
    <form method="post">
      <input type="text" id="responseBox" name="refresh_token" placeholder="未取得" />
      <input type="submit" value="REFRESH TOKEN保存" />
    </form>
  <?php } ?>
  <?php if (!empty($_POST['refresh_token'])) {
    file_put_contents("./data/token.dat", $_POST['refresh_token']);
  ?>
    <p>REFRESH TOKENを保存しました</p>
  <?php } ?>
</body>
</html>