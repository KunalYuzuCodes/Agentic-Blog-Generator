<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/evals/">
      
      
        <link rel="prev" href="../graph/">
      
      
        <link rel="next" href="../input/">
      
      
      <link rel="icon" href="../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>Evals - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../extra/tweaks.css">
    
    <script>__md_scope=new URL("..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="Evals - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/evals.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/evals/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="Evals - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/evals.png">
      
    
    
   <link href="../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#evals" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href=".." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            PydanticAI
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              Evals
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to light mode" type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to dark mode" type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7M9 21v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1m3-17a5 5 0 0 0-5 5c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58a5 5 0 0 0-5-5"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to system preference" type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 2c3.87 0 7 3.13 7 7 0 2.38-1.19 4.47-3 5.74V17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2.26C3.19 13.47 2 11.38 2 9c0-3.87 3.13-7 7-7M6 21v-1h6v1c0 .55-.45 1-1 1H7c-.55 0-1-.45-1-1M9 4C6.24 4 4 6.24 4 9c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58 0-2.76-2.24-5-5-5m10 9h-2l-3.2 9h1.9l.7-2h3.2l.7 2h1.9zm-2.15 5.65L18 15l1.15 3.65z"></path></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      <label class="md-header__button md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
      <div class="md-search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" id="searchbox" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" required="">
      <label class="md-search__icon md-icon" for="__search">

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5Z"></path></svg>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11h12Z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">

        <button id="searchbox-clear" type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">

          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41Z"></path></svg>
        </button>
      </nav>

        <div class="md-search__suggest"></div>

    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result">
          <div class="md-search-result__meta" id="type-to-start-searching">Type to start searching</div>
          <ol class="md-search-result__list" id="hits" role="presentation" hidden=""></ol>
        </div>
      </div>
    </div>
  </div>
</div>
    
    
      <div class="md-header__source">
        <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href=".." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    PydanticAI
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href=".." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6" checked="">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#installation" class="md-nav__link">
    <span class="md-ellipsis">
      Installation
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#datasets-and-cases" class="md-nav__link">
    <span class="md-ellipsis">
      Datasets and Cases
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      Evaluators
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#evaluation-process" class="md-nav__link">
    <span class="md-ellipsis">
      Evaluation Process
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#evaluation-with-llmjudge" class="md-nav__link">
    <span class="md-ellipsis">
      Evaluation with LLMJudge
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#saving-and-loading-datasets" class="md-nav__link">
    <span class="md-ellipsis">
      Saving and Loading Datasets
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#parallel-evaluation" class="md-nav__link">
    <span class="md-ellipsis">
      Parallel Evaluation
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#opentelemetry-integration" class="md-nav__link">
    <span class="md-ellipsis">
      OpenTelemetry Integration
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#generating-test-datasets" class="md-nav__link">
    <span class="md-ellipsis">
      Generating Test Datasets
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#integration-with-logfire" class="md-nav__link">
    <span class="md-ellipsis">
      Integration with Logfire
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../mcp/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    MCP
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6_14" id="__nav_6_14_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_14">
            <span class="md-nav__icon md-icon"></span>
            MCP
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../examples/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/generation/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.generation
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 474px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#installation" class="md-nav__link">
    <span class="md-ellipsis">
      Installation
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#datasets-and-cases" class="md-nav__link">
    <span class="md-ellipsis">
      Datasets and Cases
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      Evaluators
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#evaluation-process" class="md-nav__link">
    <span class="md-ellipsis">
      Evaluation Process
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#evaluation-with-llmjudge" class="md-nav__link">
    <span class="md-ellipsis">
      Evaluation with LLMJudge
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#saving-and-loading-datasets" class="md-nav__link">
    <span class="md-ellipsis">
      Saving and Loading Datasets
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#parallel-evaluation" class="md-nav__link">
    <span class="md-ellipsis">
      Parallel Evaluation
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#opentelemetry-integration" class="md-nav__link">
    <span class="md-ellipsis">
      OpenTelemetry Integration
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#generating-test-datasets" class="md-nav__link">
    <span class="md-ellipsis">
      Generating Test Datasets
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#integration-with-logfire" class="md-nav__link">
    <span class="md-ellipsis">
      Integration with Logfire
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="evals">Evals</h1>
<p>"Evals" refers to evaluating a model's performance for a specific application.</p>
<div class="admonition danger">
<p class="admonition-title">Warning</p>
<p>Unlike unit tests, evals are an emerging art/science; anyone who claims to know for sure exactly how your evals should be defined can safely be ignored.</p>
</div>
<p>Pydantic Evals is a powerful evaluation framework designed to help you systematically test and evaluate the performance and accuracy of the systems you build, especially when working with LLMs.</p>
<p>We've designed Pydantic Evals to be useful while not being too opinionated since we (along with everyone else) are still figuring out best practices. We'd love your <a href="../help/">feedback</a> on the package and how we can improve it.</p>
<div class="admonition note">
<p class="admonition-title">In Beta</p>
<p>Pydantic Evals support was <a href="https://github.com/pydantic/pydantic-ai/pull/935">introduced</a> in v0.0.47 and is currently in beta. The API is subject to change and the documentation is incomplete.</p>
</div>
<h2 id="installation">Installation</h2>
<p>To install the Pydantic Evals package, run:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="1:2" style="--md-indicator-x: 0px; --md-indicator-width: 50px;"><input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"><input id="__tabbed_1_2" name="__tabbed_1" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_1_1"><a href="#__tabbed_1_1" tabindex="-1">pip</a></label><label for="__tabbed_1_2"><a href="#__tabbed_1_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span>pydantic-evals
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code>uv<span class="w"> </span>add<span class="w"> </span>pydantic-evals
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<p><code>pydantic-evals</code> does not depend on <code>pydantic-ai</code>, but has an optional dependency on <code>logfire</code> if you'd like to
use OpenTelemetry traces in your evals, or send evaluation results to <a href="https://pydantic.dev/logfire">logfire</a>.</p>
<div class="tabbed-set tabbed-alternate" data-tabs="2:2" style="--md-indicator-x: 0px; --md-indicator-width: 50px;"><input checked="checked" id="__tabbed_2_1" name="__tabbed_2" type="radio"><input id="__tabbed_2_2" name="__tabbed_2" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_2_1"><a href="#__tabbed_2_1" tabindex="-1">pip</a></label><label for="__tabbed_2_2"><a href="#__tabbed_2_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span><span class="s1">'pydantic-evals[logfire]'</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code>uv<span class="w"> </span>add<span class="w"> </span><span class="s1">'pydantic-evals[logfire]'</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h2 id="datasets-and-cases">Datasets and Cases</h2>
<p>In Pydantic Evals, everything begins with <code>Dataset</code>s and <code>Case</code>s:</p>
<ul>
<li><a class="autorefs autorefs-internal" href="../api/pydantic_evals/dataset/#pydantic_evals.dataset.Case"><code>Case</code></a>: A single test scenario corresponding to "task" inputs. Can also optionally have a name, expected outputs, metadata, and evaluators.</li>
<li><a class="autorefs autorefs-internal" href="../api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset"><code>Dataset</code></a>: A collection of test cases designed for the evaluation of a specific task or function.</li>
</ul>
<div class="language-python highlight"><span class="filename">simple_eval_dataset.py</span><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Case</span><span class="p">,</span> <span class="n">Dataset</span>

<span class="n">case1</span> <span class="o">=</span> <span class="n">Case</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s1">'simple_case'</span><span class="p">,</span>
    <span class="n">inputs</span><span class="o">=</span><span class="s1">'What is the capital of France?'</span><span class="p">,</span>
    <span class="n">expected_output</span><span class="o">=</span><span class="s1">'Paris'</span><span class="p">,</span>
    <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s1">'difficulty'</span><span class="p">:</span> <span class="s1">'easy'</span><span class="p">},</span>
<span class="p">)</span>

<span class="n">dataset</span> <span class="o">=</span> <span class="n">Dataset</span><span class="p">(</span><span class="n">cases</span><span class="o">=</span><span class="p">[</span><span class="n">case1</span><span class="p">])</span>
</code></pre></div>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="evaluators">Evaluators</h2>
<p>Evaluators are the components that analyze and score the results of your task when tested against a case.</p>
<p>Pydantic Evals includes several built-in evaluators and allows you to create custom evaluators:</p>
<div class="language-python highlight"><span class="filename">simple_eval_evaluator.py</span><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">simple_eval_dataset</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataset</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.evaluators</span><span class="w"> </span><span class="kn">import</span> <span class="n">Evaluator</span><span class="p">,</span> <span class="n">EvaluatorContext</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.evaluators.common</span><span class="w"> </span><span class="kn">import</span> <span class="n">IsInstance</span>

<span class="n">dataset</span><span class="o">.</span><span class="n">add_evaluator</span><span class="p">(</span><span class="n">IsInstance</span><span class="p">(</span><span class="n">type_name</span><span class="o">=</span><span class="s1">'str'</span><span class="p">))</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 452px; --md-tooltip-y: 153px; --md-tooltip-0: -16px;"><a href="#__code_5_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">MyEvaluator</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">):</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 624px; --md-tooltip-y: 249px; --md-tooltip-0: -16px;"><a href="#__code_5_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
        <span class="k">if</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span> <span class="o">==</span> <span class="n">ctx</span><span class="o">.</span><span class="n">expected_output</span><span class="p">:</span>
            <span class="k">return</span> <span class="mf">1.0</span>
        <span class="k">elif</span> <span class="p">(</span>
            <span class="nb">isinstance</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span>
            <span class="ow">and</span> <span class="n">ctx</span><span class="o">.</span><span class="n">expected_output</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="mf">0.8</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="mf">0.0</span>


<span class="n">dataset</span><span class="o">.</span><span class="n">add_evaluator</span><span class="p">(</span><span class="n">MyEvaluator</span><span class="p">())</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="evaluation-process">Evaluation Process</h2>
<p>The evaluation process involves running a task against all cases in a dataset:</p>
<p>Putting the above two examples together and using the more declarative <code>evaluators</code> kwarg to <a class="autorefs autorefs-internal" href="../api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset"><code>Dataset</code></a>:</p>
<div class="language-python highlight"><span class="filename">simple_eval_complete.py</span><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Case</span><span class="p">,</span> <span class="n">Dataset</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.evaluators</span><span class="w"> </span><span class="kn">import</span> <span class="n">Evaluator</span><span class="p">,</span> <span class="n">EvaluatorContext</span><span class="p">,</span> <span class="n">IsInstance</span>

<span class="n">case1</span> <span class="o">=</span> <span class="n">Case</span><span class="p">(</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 150px; --md-tooltip-y: 77px; --md-tooltip-0: -16px;"><a href="#__code_6_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
    <span class="n">name</span><span class="o">=</span><span class="s1">'simple_case'</span><span class="p">,</span>
    <span class="n">inputs</span><span class="o">=</span><span class="s1">'What is the capital of France?'</span><span class="p">,</span>
    <span class="n">expected_output</span><span class="o">=</span><span class="s1">'Paris'</span><span class="p">,</span>
    <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s1">'difficulty'</span><span class="p">:</span> <span class="s1">'easy'</span><span class="p">},</span>
<span class="p">)</span>


<span class="k">class</span><span class="w"> </span><span class="nc">MyEvaluator</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]):</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span> <span class="o">==</span> <span class="n">ctx</span><span class="o">.</span><span class="n">expected_output</span><span class="p">:</span>
            <span class="k">return</span> <span class="mf">1.0</span>
        <span class="k">elif</span> <span class="p">(</span>
            <span class="nb">isinstance</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span>
            <span class="ow">and</span> <span class="n">ctx</span><span class="o">.</span><span class="n">expected_output</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="mf">0.8</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="mf">0.0</span>


<span class="n">dataset</span> <span class="o">=</span> <span class="n">Dataset</span><span class="p">(</span>
    <span class="n">cases</span><span class="o">=</span><span class="p">[</span><span class="n">case1</span><span class="p">],</span>
    <span class="n">evaluators</span><span class="o">=</span><span class="p">[</span><span class="n">IsInstance</span><span class="p">(</span><span class="n">type_name</span><span class="o">=</span><span class="s1">'str'</span><span class="p">),</span> <span class="n">MyEvaluator</span><span class="p">()],</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 534px; --md-tooltip-y: 515px; --md-tooltip-0: -16px;"><a href="#__code_6_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
<span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">guess_city</span><span class="p">(</span><span class="n">question</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 395px; --md-tooltip-y: 591px; --md-tooltip-0: -16px;"><a href="#__code_6_annotation_4" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="4"></span></a></aside></span>
    <span class="k">return</span> <span class="s1">'Paris'</span>


<span class="n">report</span> <span class="o">=</span> <span class="n">dataset</span><span class="o">.</span><span class="n">evaluate_sync</span><span class="p">(</span><span class="n">guess_city</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 387px; --md-tooltip-y: 667px; --md-tooltip-0: -16px;"><a href="#__code_6_annotation_5" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="5"></span></a></aside></span>
<span class="n">report</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">include_input</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_durations</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 681px; --md-tooltip-y: 686px; --md-tooltip-0: -16px;"><a href="#__code_6_annotation_6" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="6"></span></a></aside></span>
<span class="sd">"""</span>
<span class="sd">                              Evaluation Summary: guess_city</span>
<span class="sd">┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓</span>
<span class="sd">┃ Case ID     ┃ Inputs                         ┃ Outputs ┃ Scores            ┃ Assertions ┃</span>
<span class="sd">┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩</span>
<span class="sd">│ simple_case │ What is the capital of France? │ Paris   │ MyEvaluator: 1.00 │ ✔          │</span>
<span class="sd">├─────────────┼────────────────────────────────┼─────────┼───────────────────┼────────────┤</span>
<span class="sd">│ Averages    │                                │         │ MyEvaluator: 1.00 │ 100.0% ✔   │</span>
<span class="sd">└─────────────┴────────────────────────────────┴─────────┴───────────────────┴────────────┘</span>
<span class="sd">"""</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li>Also create a custom evaluator function as above</li>
<li></li>
<li></li>
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="evaluation-with-llmjudge">Evaluation with <code>LLMJudge</code></h2>
<p>In this example we evaluate a method for generating recipes based on customer orders.</p>
<div class="language-python highlight"><span class="filename">judge_recipes.py</span><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">__future__</span><span class="w"> </span><span class="kn">import</span> <span class="n">annotations</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Any</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.format_as_xml</span><span class="w"> </span><span class="kn">import</span> <span class="n">format_as_xml</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Case</span><span class="p">,</span> <span class="n">Dataset</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.evaluators</span><span class="w"> </span><span class="kn">import</span> <span class="n">IsInstance</span><span class="p">,</span> <span class="n">LLMJudge</span>


<span class="k">class</span><span class="w"> </span><span class="nc">CustomerOrder</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 297px; --md-tooltip-y: 249px; --md-tooltip-0: -16px;"><a href="#__code_7_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
    <span class="n">dish_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">dietary_restriction</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>


<span class="k">class</span><span class="w"> </span><span class="nc">Recipe</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">ingredients</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">steps</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>


<span class="n">recipe_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'groq:llama-3.3-70b-versatile'</span><span class="p">,</span>
    <span class="n">result_type</span><span class="o">=</span><span class="n">Recipe</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="p">(</span>
        <span class="s1">'Generate a recipe to cook the dish that meets the dietary restrictions.'</span>
    <span class="p">),</span>
<span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">transform_recipe</span><span class="p">(</span><span class="n">customer_order</span><span class="p">:</span> <span class="n">CustomerOrder</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Recipe</span><span class="p">:</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 599px; --md-tooltip-y: 610px; --md-tooltip-0: -16px;"><a href="#__code_7_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
    <span class="n">r</span> <span class="o">=</span> <span class="k">await</span> <span class="n">recipe_agent</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">format_as_xml</span><span class="p">(</span><span class="n">customer_order</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">r</span><span class="o">.</span><span class="n">data</span>


<span class="n">recipe_dataset</span> <span class="o">=</span> <span class="n">Dataset</span><span class="p">[</span><span class="n">CustomerOrder</span><span class="p">,</span> <span class="n">Recipe</span><span class="p">,</span> <span class="n">Any</span><span class="p">](</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 477px; --md-tooltip-y: 705px; --md-tooltip-0: -16px;"><a href="#__code_7_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
    <span class="n">cases</span><span class="o">=</span><span class="p">[</span>
        <span class="n">Case</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s1">'vegetarian_recipe'</span><span class="p">,</span>
            <span class="n">inputs</span><span class="o">=</span><span class="n">CustomerOrder</span><span class="p">(</span>
                <span class="n">dish_name</span><span class="o">=</span><span class="s1">'Spaghetti Bolognese'</span><span class="p">,</span> <span class="n">dietary_restriction</span><span class="o">=</span><span class="s1">'vegetarian'</span>
            <span class="p">),</span>
            <span class="n">expected_output</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>  <span class="c1"># <aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 330px; --md-tooltip-y: 839px; --md-tooltip-0: -16px;"><a href="#__code_7_annotation_4" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="4"></span></a></aside></span>
            <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s1">'focus'</span><span class="p">:</span> <span class="s1">'vegetarian'</span><span class="p">},</span>
            <span class="n">evaluators</span><span class="o">=</span><span class="p">(</span>
                <span class="n">LLMJudge</span><span class="p">(</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 248px; --md-tooltip-y: 896px; --md-tooltip-0: -16px;"><a href="#__code_7_annotation_5" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="5"></span></a></aside></span>
                    <span class="n">rubric</span><span class="o">=</span><span class="s1">'Recipe should not contain meat or animal products'</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">Case</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s1">'gluten_free_recipe'</span><span class="p">,</span>
            <span class="n">inputs</span><span class="o">=</span><span class="n">CustomerOrder</span><span class="p">(</span>
                <span class="n">dish_name</span><span class="o">=</span><span class="s1">'Chocolate Cake'</span><span class="p">,</span> <span class="n">dietary_restriction</span><span class="o">=</span><span class="s1">'gluten-free'</span>
            <span class="p">),</span>
            <span class="n">expected_output</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s1">'focus'</span><span class="p">:</span> <span class="s1">'gluten-free'</span><span class="p">},</span>
            <span class="c1"># Case-specific evaluator with a focused rubric</span>
            <span class="n">evaluators</span><span class="o">=</span><span class="p">(</span>
                <span class="n">LLMJudge</span><span class="p">(</span>
                    <span class="n">rubric</span><span class="o">=</span><span class="s1">'Recipe should not contain gluten or wheat products'</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">),</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">evaluators</span><span class="o">=</span><span class="p">[</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 175px; --md-tooltip-y: 1277px; --md-tooltip-0: -16px;"><a href="#__code_7_annotation_6" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="6"></span></a></aside></span>
        <span class="n">IsInstance</span><span class="p">(</span><span class="n">type_name</span><span class="o">=</span><span class="s1">'Recipe'</span><span class="p">),</span>
        <span class="n">LLMJudge</span><span class="p">(</span>
            <span class="n">rubric</span><span class="o">=</span><span class="s1">'Recipe should have clear steps and relevant ingredients'</span><span class="p">,</span>
            <span class="n">include_input</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="s1">'anthropic:claude-3-7-sonnet-latest'</span><span class="p">,</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 493px; --md-tooltip-y: 1372px; --md-tooltip-0: -16px;"><a href="#__code_7_annotation_7" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="7"></span></a></aside></span>
        <span class="p">),</span>
    <span class="p">],</span>
<span class="p">)</span>


<span class="n">report</span> <span class="o">=</span> <span class="n">recipe_dataset</span><span class="o">.</span><span class="n">evaluate_sync</span><span class="p">(</span><span class="n">transform_recipe</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">report</span><span class="p">)</span>
<span class="sd">"""</span>
<span class="sd">     Evaluation Summary: transform_recipe</span>
<span class="sd">┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓</span>
<span class="sd">┃ Case ID            ┃ Assertions ┃ Duration ┃</span>
<span class="sd">┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩</span>
<span class="sd">│ vegetarian_recipe  │ ✔✔✔        │     10ms │</span>
<span class="sd">├────────────────────┼────────────┼──────────┤</span>
<span class="sd">│ gluten_free_recipe │ ✔✔✔        │     10ms │</span>
<span class="sd">├────────────────────┼────────────┼──────────┤</span>
<span class="sd">│ Averages           │ 100.0% ✔   │     10ms │</span>
<span class="sd">└────────────────────┴────────────┴──────────┘</span>
<span class="sd">"""</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="saving-and-loading-datasets">Saving and Loading Datasets</h2>
<p>Datasets can be saved to and loaded from YAML or JSON files.</p>
<div class="language-python highlight"><span class="filename">save_load_dataset_example.py</span><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pathlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">Path</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">judge_recipes</span><span class="w"> </span><span class="kn">import</span> <span class="n">CustomerOrder</span><span class="p">,</span> <span class="n">Recipe</span><span class="p">,</span> <span class="n">recipe_dataset</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Dataset</span>

<span class="n">recipe_transforms_file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="s1">'recipe_transform_tests.yaml'</span><span class="p">)</span>
<span class="n">recipe_dataset</span><span class="o">.</span><span class="n">to_file</span><span class="p">(</span><span class="n">recipe_transforms_file</span><span class="p">)</span>  <span class="c1"># (1)!</span>
<span class="nb">print</span><span class="p">(</span><span class="n">recipe_transforms_file</span><span class="o">.</span><span class="n">read_text</span><span class="p">())</span>
<span class="sd">"""</span>
<span class="sd"># yaml-language-server: $schema=recipe_transform_tests_schema.json</span>
<span class="sd">cases:</span>
<span class="sd">- name: vegetarian_recipe</span>
<span class="sd">  inputs:</span>
<span class="sd">    dish_name: Spaghetti Bolognese</span>
<span class="sd">    dietary_restriction: vegetarian</span>
<span class="sd">  metadata:</span>
<span class="sd">    focus: vegetarian</span>
<span class="sd">  evaluators:</span>
<span class="sd">  - LLMJudge: Recipe should not contain meat or animal products</span>
<span class="sd">- name: gluten_free_recipe</span>
<span class="sd">  inputs:</span>
<span class="sd">    dish_name: Chocolate Cake</span>
<span class="sd">    dietary_restriction: gluten-free</span>
<span class="sd">  metadata:</span>
<span class="sd">    focus: gluten-free</span>
<span class="sd">  evaluators:</span>
<span class="sd">  - LLMJudge: Recipe should not contain gluten or wheat products</span>
<span class="sd">evaluators:</span>
<span class="sd">- IsInstance: Recipe</span>
<span class="sd">- LLMJudge:</span>
<span class="sd">    rubric: Recipe should have clear steps and relevant ingredients</span>
<span class="sd">    model: anthropic:claude-3-7-sonnet-latest</span>
<span class="sd">    include_input: true</span>
<span class="sd">"""</span>

<span class="c1"># Load dataset from file</span>
<span class="n">loaded_dataset</span> <span class="o">=</span> <span class="n">Dataset</span><span class="p">[</span><span class="n">CustomerOrder</span><span class="p">,</span> <span class="n">Recipe</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">recipe_transforms_file</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Loaded dataset with </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">loaded_dataset</span><span class="o">.</span><span class="n">cases</span><span class="p">)</span><span class="si">}</span><span class="s1"> cases'</span><span class="p">)</span>
<span class="c1">#&gt; Loaded dataset with 2 cases</span>
</code></pre></div>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="parallel-evaluation">Parallel Evaluation</h2>
<p>You can control concurrency during evaluation (this might be useful to prevent exceeding a rate limit):</p>
<div class="language-python highlight"><span class="filename">parallel_evaluation_example.py</span><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code tabindex="0"><span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">time</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Case</span><span class="p">,</span> <span class="n">Dataset</span>

<span class="c1"># Create a dataset with multiple test cases</span>
<span class="n">dataset</span> <span class="o">=</span> <span class="n">Dataset</span><span class="p">(</span>
    <span class="n">cases</span><span class="o">=</span><span class="p">[</span>
        <span class="n">Case</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="sa">f</span><span class="s1">'case_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span>
            <span class="n">inputs</span><span class="o">=</span><span class="n">i</span><span class="p">,</span>
            <span class="n">expected_output</span><span class="o">=</span><span class="n">i</span> <span class="o">*</span> <span class="mi">2</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
    <span class="p">]</span>
<span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">double_number</span><span class="p">(</span><span class="n">input_value</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Function that simulates work by sleeping for a second before returning double the input."""</span>
    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span>  <span class="c1"># Simulate work</span>
    <span class="k">return</span> <span class="n">input_value</span> <span class="o">*</span> <span class="mi">2</span>


<span class="c1"># Run evaluation with unlimited concurrency</span>
<span class="n">t0</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
<span class="n">report_default</span> <span class="o">=</span> <span class="n">dataset</span><span class="o">.</span><span class="n">evaluate_sync</span><span class="p">(</span><span class="n">double_number</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Evaluation took less than 0.3s: </span><span class="si">{</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">t0</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mf">0.3</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
<span class="c1">#&gt; Evaluation took less than 0.3s: True</span>

<span class="n">report_default</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">include_input</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_durations</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 746px; --md-tooltip-y: 591px; --md-tooltip-0: -16px;"><a href="#__code_9_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
<span class="sd">"""</span>
<span class="sd">      Evaluation Summary:</span>
<span class="sd">         double_number</span>
<span class="sd">┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┓</span>
<span class="sd">┃ Case ID  ┃ Inputs ┃ Outputs ┃</span>
<span class="sd">┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━┩</span>
<span class="sd">│ case_0   │ 0      │ 0       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ case_1   │ 1      │ 2       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ case_2   │ 2      │ 4       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ case_3   │ 3      │ 6       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ case_4   │ 4      │ 8       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ Averages │        │         │</span>
<span class="sd">└──────────┴────────┴─────────┘</span>
<span class="sd">"""</span>

<span class="c1"># Run evaluation with limited concurrency</span>
<span class="n">t0</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
<span class="n">report_limited</span> <span class="o">=</span> <span class="n">dataset</span><span class="o">.</span><span class="n">evaluate_sync</span><span class="p">(</span><span class="n">double_number</span><span class="p">,</span> <span class="n">max_concurrency</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Evaluation took more than 0.5s: </span><span class="si">{</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">t0</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mf">0.5</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
<span class="c1">#&gt; Evaluation took more than 0.5s: True</span>

<span class="n">report_limited</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">include_input</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_durations</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 746px; --md-tooltip-y: 1105px; --md-tooltip-0: -16px;"><a href="#__code_9_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
<span class="sd">"""</span>
<span class="sd">      Evaluation Summary:</span>
<span class="sd">         double_number</span>
<span class="sd">┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┓</span>
<span class="sd">┃ Case ID  ┃ Inputs ┃ Outputs ┃</span>
<span class="sd">┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━┩</span>
<span class="sd">│ case_0   │ 0      │ 0       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ case_1   │ 1      │ 2       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ case_2   │ 2      │ 4       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ case_3   │ 3      │ 6       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ case_4   │ 4      │ 8       │</span>
<span class="sd">├──────────┼────────┼─────────┤</span>
<span class="sd">│ Averages │        │         │</span>
<span class="sd">└──────────┴────────┴─────────┘</span>
<span class="sd">"""</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="opentelemetry-integration">OpenTelemetry Integration</h2>
<p>Pydantic Evals integrates with OpenTelemetry for tracing.</p>
<p>The <a class="autorefs autorefs-internal" href="../api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorContext"><code>EvaluatorContext</code></a> includes a property called <code>span_tree</code>
which returns a <a class="autorefs autorefs-internal" href="../api/pydantic_evals/otel/#pydantic_evals.otel.SpanTree"><code>SpanTree</code></a>. The <code>SpanTree</code> provides a way to query and analyze
the spans generated during function execution. This provides a way to access the results of instrumentation during
evaluation.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If you just want to write unit tests that ensure that specific spans are produced during calls to your evaluation
task, it's usually better to just use the <code>logfire.testing.capfire</code> fixture directly.</p>
</div>
<p>There are two main ways this is useful.</p>
<!-- TODO: Finish this -->

<div class="language-python highlight"><span class="filename">opentelemetry_example.py</span><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code tabindex="0"><span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Any</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">logfire</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Case</span><span class="p">,</span> <span class="n">Dataset</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.evaluators</span><span class="w"> </span><span class="kn">import</span> <span class="n">Evaluator</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.evaluators.context</span><span class="w"> </span><span class="kn">import</span> <span class="n">EvaluatorContext</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.otel.span_tree</span><span class="w"> </span><span class="kn">import</span> <span class="n">SpanQuery</span>

<span class="n">logfire</span><span class="o">.</span><span class="n">configure</span><span class="p">(</span>  <span class="c1"># ensure that an OpenTelemetry tracer is configured</span>
    <span class="n">send_to_logfire</span><span class="o">=</span><span class="s1">'if-token-present'</span>
<span class="p">)</span>


<span class="k">class</span><span class="w"> </span><span class="nc">SpanTracingEvaluator</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Evaluator that analyzes the span tree generated during function execution."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="c1"># Get the span tree from the context</span>
        <span class="n">span_tree</span> <span class="o">=</span> <span class="n">ctx</span><span class="o">.</span><span class="n">span_tree</span>
        <span class="k">if</span> <span class="n">span_tree</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">{</span><span class="s1">'has_spans'</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span> <span class="s1">'performance_score'</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">}</span>

        <span class="c1"># Find all spans with "processing" in the name</span>
        <span class="n">processing_spans</span> <span class="o">=</span> <span class="n">span_tree</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="k">lambda</span> <span class="n">node</span><span class="p">:</span> <span class="s1">'processing'</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

        <span class="c1"># Calculate total processing time</span>
        <span class="n">total_processing_time</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span>
            <span class="p">(</span><span class="n">span</span><span class="o">.</span><span class="n">duration</span><span class="o">.</span><span class="n">total_seconds</span><span class="p">()</span> <span class="k">for</span> <span class="n">span</span> <span class="ow">in</span> <span class="n">processing_spans</span><span class="p">),</span> <span class="mf">0.0</span>
        <span class="p">)</span>

        <span class="c1"># Check for error spans</span>
        <span class="n">error_query</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'name_contains'</span><span class="p">:</span> <span class="s1">'error'</span><span class="p">}</span>
        <span class="n">has_errors</span> <span class="o">=</span> <span class="n">span_tree</span><span class="o">.</span><span class="n">any</span><span class="p">(</span><span class="n">error_query</span><span class="p">)</span>

        <span class="c1"># Calculate a performance score (lower is better)</span>
        <span class="n">performance_score</span> <span class="o">=</span> <span class="mf">1.0</span> <span class="k">if</span> <span class="n">total_processing_time</span> <span class="o">&lt;</span> <span class="mf">0.5</span> <span class="k">else</span> <span class="mf">0.5</span>

        <span class="k">return</span> <span class="p">{</span>
            <span class="s1">'has_spans'</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
            <span class="s1">'has_errors'</span><span class="p">:</span> <span class="n">has_errors</span><span class="p">,</span>
            <span class="s1">'performance_score'</span><span class="p">:</span> <span class="mi">0</span> <span class="k">if</span> <span class="n">has_errors</span> <span class="k">else</span> <span class="n">performance_score</span><span class="p">,</span>
        <span class="p">}</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">process_text</span><span class="p">(</span><span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Function that processes text with OpenTelemetry instrumentation."""</span>
    <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'process_text'</span><span class="p">):</span>
        <span class="c1"># Simulate initial processing</span>
        <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'text_processing'</span><span class="p">):</span>
            <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span>
            <span class="n">processed</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>

        <span class="c1"># Simulate additional processing</span>
        <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'additional_processing'</span><span class="p">):</span>
            <span class="k">if</span> <span class="s1">'error'</span> <span class="ow">in</span> <span class="n">processed</span><span class="p">:</span>
                <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'error_handling'</span><span class="p">):</span>
                    <span class="n">logfire</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Error detected in text: </span><span class="si">{</span><span class="n">text</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
                    <span class="k">return</span> <span class="sa">f</span><span class="s1">'Error processing: </span><span class="si">{</span><span class="n">text</span><span class="si">}</span><span class="s1">'</span>
            <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.2</span><span class="p">)</span>
            <span class="n">processed</span> <span class="o">=</span> <span class="n">processed</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">' '</span><span class="p">,</span> <span class="s1">'_'</span><span class="p">)</span>

        <span class="k">return</span> <span class="sa">f</span><span class="s1">'Processed: </span><span class="si">{</span><span class="n">processed</span><span class="si">}</span><span class="s1">'</span>


<span class="c1"># Create test cases</span>
<span class="n">dataset</span> <span class="o">=</span> <span class="n">Dataset</span><span class="p">(</span>
    <span class="n">cases</span><span class="o">=</span><span class="p">[</span>
        <span class="n">Case</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s1">'normal_text'</span><span class="p">,</span>
            <span class="n">inputs</span><span class="o">=</span><span class="s1">'Hello World'</span><span class="p">,</span>
            <span class="n">expected_output</span><span class="o">=</span><span class="s1">'Processed: hello_world'</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">Case</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s1">'text_with_error'</span><span class="p">,</span>
            <span class="n">inputs</span><span class="o">=</span><span class="s1">'Contains error marker'</span><span class="p">,</span>
            <span class="n">expected_output</span><span class="o">=</span><span class="s1">'Error processing: Contains error marker'</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">evaluators</span><span class="o">=</span><span class="p">[</span><span class="n">SpanTracingEvaluator</span><span class="p">()],</span>
<span class="p">)</span>

<span class="c1"># Run evaluation - spans are automatically captured since logfire is configured</span>
<span class="n">report</span> <span class="o">=</span> <span class="n">dataset</span><span class="o">.</span><span class="n">evaluate_sync</span><span class="p">(</span><span class="n">process_text</span><span class="p">)</span>

<span class="c1"># Print the report</span>
<span class="n">report</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">include_input</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_durations</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 681px; --md-tooltip-y: 1676px; --md-tooltip-0: -16px;"><a href="#__code_10_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
<span class="sd">"""</span>
<span class="sd">                                              Evaluation Summary: process_text</span>
<span class="sd">┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓</span>
<span class="sd">┃ Case ID         ┃ Inputs                ┃ Outputs                                 ┃ Scores                   ┃ Assertions ┃</span>
<span class="sd">┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩</span>
<span class="sd">│ normal_text     │ Hello World           │ Processed: hello_world                  │ performance_score: 1.00  │ ✔✗         │</span>
<span class="sd">├─────────────────┼───────────────────────┼─────────────────────────────────────────┼──────────────────────────┼────────────┤</span>
<span class="sd">│ text_with_error │ Contains error marker │ Error processing: Contains error marker │ performance_score: 0     │ ✔✔         │</span>
<span class="sd">├─────────────────┼───────────────────────┼─────────────────────────────────────────┼──────────────────────────┼────────────┤</span>
<span class="sd">│ Averages        │                       │                                         │ performance_score: 0.500 │ 75.0% ✔    │</span>
<span class="sd">└─────────────────┴───────────────────────┴─────────────────────────────────────────┴──────────────────────────┴────────────┘</span>
<span class="sd">"""</span>
</code></pre></div>
<ol hidden="">
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="generating-test-datasets">Generating Test Datasets</h2>
<p>Pydantic Evals allows you to generate test datasets using LLMs with <a class="autorefs autorefs-internal" href="../api/pydantic_evals/generation/#pydantic_evals.generation.generate_dataset"><code>generate_dataset</code></a>.</p>
<p>Datasets can be generated in either JSON or YAML format, in both cases a JSON schema file is generated alongside the dataset and referenced in the dataset, so you should get type checking and auto-completion in your editor.</p>
<div class="language-python highlight"><span class="filename">generate_dataset_example.py</span><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">__future__</span><span class="w"> </span><span class="kn">import</span> <span class="n">annotations</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pathlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">Path</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span><span class="p">,</span> <span class="n">Field</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Dataset</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.generation</span><span class="w"> </span><span class="kn">import</span> <span class="n">generate_dataset</span>


<span class="k">class</span><span class="w"> </span><span class="nc">QuestionInputs</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">use_attribute_docstrings</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 559px; --md-tooltip-y: 210px; --md-tooltip-0: -16px;"><a href="#__code_11_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
<span class="w">    </span><span class="sd">"""Model for question inputs."""</span>

    <span class="n">question</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""A question to answer"""</span>
    <span class="n">context</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Optional context for the question"""</span>


<span class="k">class</span><span class="w"> </span><span class="nc">AnswerOutput</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">use_attribute_docstrings</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 542px; --md-tooltip-y: 382px; --md-tooltip-0: -16px;"><a href="#__code_11_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
<span class="w">    </span><span class="sd">"""Model for expected answer outputs."""</span>

    <span class="n">answer</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The answer to the question"""</span>
    <span class="n">confidence</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">ge</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">le</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""Confidence level (0-1)"""</span>


<span class="k">class</span><span class="w"> </span><span class="nc">MetadataType</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">use_attribute_docstrings</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 542px; --md-tooltip-y: 553px; --md-tooltip-0: -16px;"><a href="#__code_11_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
<span class="w">    </span><span class="sd">"""Metadata model for test cases."""</span>

    <span class="n">difficulty</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""Difficulty level (easy, medium, hard)"""</span>
    <span class="n">category</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""Question category"""</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">dataset</span> <span class="o">=</span> <span class="k">await</span> <span class="n">generate_dataset</span><span class="p">(</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 346px; --md-tooltip-y: 744px; --md-tooltip-0: -16px;"><a href="#__code_11_annotation_4" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="4"></span></a></aside></span>
        <span class="n">dataset_type</span><span class="o">=</span><span class="n">Dataset</span><span class="p">[</span><span class="n">QuestionInputs</span><span class="p">,</span> <span class="n">AnswerOutput</span><span class="p">,</span> <span class="n">MetadataType</span><span class="p">],</span>
        <span class="n">n_examples</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
        <span class="n">extra_instructions</span><span class="o">=</span><span class="s2">"""</span>
<span class="s2">        Generate question-answer pairs about world capitals and landmarks.</span>
<span class="s2">        Make sure to include both easy and challenging questions.</span>
<span class="s2">        """</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">output_file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="s1">'questions_cases.yaml'</span><span class="p">)</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">to_file</span><span class="p">(</span><span class="n">output_file</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 306px; --md-tooltip-y: 915px; --md-tooltip-0: -16px;"><a href="#__code_11_annotation_5" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="5"></span></a></aside></span>
    <span class="nb">print</span><span class="p">(</span><span class="n">output_file</span><span class="o">.</span><span class="n">read_text</span><span class="p">())</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    # yaml-language-server: $schema=questions_cases_schema.json</span>
<span class="sd">    cases:</span>
<span class="sd">    - name: Easy Capital Question</span>
<span class="sd">      inputs:</span>
<span class="sd">        question: What is the capital of France?</span>
<span class="sd">      metadata:</span>
<span class="sd">        difficulty: easy</span>
<span class="sd">        category: Geography</span>
<span class="sd">      expected_output:</span>
<span class="sd">        answer: Paris</span>
<span class="sd">        confidence: 0.95</span>
<span class="sd">      evaluators:</span>
<span class="sd">      - EqualsExpected</span>
<span class="sd">    - name: Challenging Landmark Question</span>
<span class="sd">      inputs:</span>
<span class="sd">        question: Which world-famous landmark is located on the banks of the Seine River?</span>
<span class="sd">      metadata:</span>
<span class="sd">        difficulty: hard</span>
<span class="sd">        category: Landmarks</span>
<span class="sd">      expected_output:</span>
<span class="sd">        answer: Eiffel Tower</span>
<span class="sd">        confidence: 0.9</span>
<span class="sd">      evaluators:</span>
<span class="sd">      - EqualsExpected</span>
<span class="sd">    """</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is" — you'll need to add <code>asyncio.run(main(answer))</code> to run <code>main</code>)</em></p>
<p>You can also write datasets as JSON files:</p>
<div class="language-python highlight"><span class="filename">generate_dataset_example_json.py</span><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">pathlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">Path</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">generate_dataset_example</span><span class="w"> </span><span class="kn">import</span> <span class="n">AnswerOutput</span><span class="p">,</span> <span class="n">MetadataType</span><span class="p">,</span> <span class="n">QuestionInputs</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Dataset</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.generation</span><span class="w"> </span><span class="kn">import</span> <span class="n">generate_dataset</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">dataset</span> <span class="o">=</span> <span class="k">await</span> <span class="n">generate_dataset</span><span class="p">(</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 346px; --md-tooltip-y: 191px; --md-tooltip-0: -16px;"><a href="#__code_12_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
        <span class="n">dataset_type</span><span class="o">=</span><span class="n">Dataset</span><span class="p">[</span><span class="n">QuestionInputs</span><span class="p">,</span> <span class="n">AnswerOutput</span><span class="p">,</span> <span class="n">MetadataType</span><span class="p">],</span>
        <span class="n">n_examples</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
        <span class="n">extra_instructions</span><span class="o">=</span><span class="s2">"""</span>
<span class="s2">        Generate question-answer pairs about world capitals and landmarks.</span>
<span class="s2">        Make sure to include both easy and challenging questions.</span>
<span class="s2">        """</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">output_file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="s1">'questions_cases.json'</span><span class="p">)</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">to_file</span><span class="p">(</span><span class="n">output_file</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 306px; --md-tooltip-y: 363px; --md-tooltip-0: -16px;"><a href="#__code_12_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
    <span class="nb">print</span><span class="p">(</span><span class="n">output_file</span><span class="o">.</span><span class="n">read_text</span><span class="p">())</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    {</span>
<span class="sd">      "$schema": "questions_cases_schema.json",</span>
<span class="sd">      "cases": [</span>
<span class="sd">        {</span>
<span class="sd">          "name": "Easy Capital Question",</span>
<span class="sd">          "inputs": {</span>
<span class="sd">            "question": "What is the capital of France?"</span>
<span class="sd">          },</span>
<span class="sd">          "metadata": {</span>
<span class="sd">            "difficulty": "easy",</span>
<span class="sd">            "category": "Geography"</span>
<span class="sd">          },</span>
<span class="sd">          "expected_output": {</span>
<span class="sd">            "answer": "Paris",</span>
<span class="sd">            "confidence": 0.95</span>
<span class="sd">          },</span>
<span class="sd">          "evaluators": [</span>
<span class="sd">            "EqualsExpected"</span>
<span class="sd">          ]</span>
<span class="sd">        },</span>
<span class="sd">        {</span>
<span class="sd">          "name": "Challenging Landmark Question",</span>
<span class="sd">          "inputs": {</span>
<span class="sd">            "question": "Which world-famous landmark is located on the banks of the Seine River?"</span>
<span class="sd">          },</span>
<span class="sd">          "metadata": {</span>
<span class="sd">            "difficulty": "hard",</span>
<span class="sd">            "category": "Landmarks"</span>
<span class="sd">          },</span>
<span class="sd">          "expected_output": {</span>
<span class="sd">            "answer": "Eiffel Tower",</span>
<span class="sd">            "confidence": 0.9</span>
<span class="sd">          },</span>
<span class="sd">          "evaluators": [</span>
<span class="sd">            "EqualsExpected"</span>
<span class="sd">          ]</span>
<span class="sd">        }</span>
<span class="sd">      ]</span>
<span class="sd">    }</span>
<span class="sd">    """</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is" — you'll need to add <code>asyncio.run(main(answer))</code> to run <code>main</code>)</em></p>
<h2 id="integration-with-logfire">Integration with Logfire</h2>
<p>Pydantic Evals is implemented using OpenTelemetry to record traces of the evaluation process. These traces contain all
the information included in the terminal output as attributes, but also include full tracing from the executions of the
evaluation task function.</p>
<p>You can send these traces to any OpenTelemetry-compatible backend, including <a href="https://logfire.pydantic.dev/docs">Pydantic Logfire</a>.</p>
<p>All you need to do is configure Logfire via <code>logfire.configure</code>:</p>
<div class="language-python highlight"><span class="filename">logfire_integration.py</span><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="kn">import</span><span class="w"> </span><span class="nn">logfire</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">judge_recipes</span><span class="w"> </span><span class="kn">import</span> <span class="n">recipe_dataset</span><span class="p">,</span> <span class="n">transform_recipe</span>

<span class="n">logfire</span><span class="o">.</span><span class="n">configure</span><span class="p">(</span>
    <span class="n">send_to_logfire</span><span class="o">=</span><span class="s1">'if-token-present'</span><span class="p">,</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 363px; --md-tooltip-y: 96px; --md-tooltip-0: -16px;"><a href="#__code_13_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
    <span class="n">environment</span><span class="o">=</span><span class="s1">'development'</span><span class="p">,</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 289px; --md-tooltip-y: 115px; --md-tooltip-0: -16px;"><a href="#__code_13_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
    <span class="n">service_name</span><span class="o">=</span><span class="s1">'evals'</span><span class="p">,</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 248px; --md-tooltip-y: 134px; --md-tooltip-0: -16px;"><a href="#__code_13_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
<span class="p">)</span>

<span class="n">recipe_dataset</span><span class="o">.</span><span class="n">evaluate_sync</span><span class="p">(</span><span class="n">transform_recipe</span><span class="p">)</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
</ol>
<p>Logfire has some special integration with Pydantic Evals traces, including a table view of the evaluation results
on the evaluation root span (which is generated in each call to <a class="autorefs autorefs-internal" href="../api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset.evaluate"><code>Dataset.evaluate</code></a>):</p>
<p><a class="glightbox" href="../img/logfire-evals-overview.png" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img alt="Logfire Evals Overview" src="../img/logfire-evals-overview.png" width="3456" height="1832"></a></p>
<p>and a detailed view of the inputs and outputs for the execution of each case:</p>
<p><a class="glightbox" href="../img/logfire-evals-case.png" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img alt="Logfire Evals Case" src="../img/logfire-evals-case.png" width="3456" height="1836"></a></p>
<p>In addition, any OpenTelemetry spans generated during the evaluation process will be sent to Logfire, allowing you to
visualize the full execution of the code called during the evaluation process:</p>
<p><a class="glightbox" href="../img/logfire-evals-case-trace.png" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img alt="Logfire Evals Case Trace" src="../img/logfire-evals-case-trace.png" width="3456" height="1836"></a></p>
<p>This can be especially helpful when attempting to write evaluators that make use of the <code>span_tree</code> property of the
<a class="autorefs autorefs-internal" href="../api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorContext"><code>EvaluatorContext</code></a>, as described in the
<a href="#opentelemetry-integration">OpenTelemetry Integration</a> section above.</p>
<p>This allows you to write evaluations that depend on information about which code paths were executed during the call to
the task function without needing to manually instrument the code being evaluated, as long as the code being evaluated
is already adequately instrumented with OpenTelemetry. In the case of PydanticAI agents, for example, this can be used
to ensure specific tools are (or are not) called during the execution of specific cases.</p>
<p>Using OpenTelemetry in this way also means that all data used to evaluate the task executions will be accessible in
the traces produced by production runs of the code, making it straightforward to perform the same evaluations on
production data.</p>







  
  






                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
    <div class="md-copyright__highlight">
      © Pydantic Services Inc. 2024 to present
    </div>
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    <script id="__config" type="application/json">{"base": "..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>